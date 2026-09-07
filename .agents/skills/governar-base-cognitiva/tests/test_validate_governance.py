import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate_governance.py"
SPEC = importlib.util.spec_from_file_location("validate_governance", SCRIPT)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATOR)


class DynamicGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        subprocess.run(("git", "init", "-q"), cwd=self.root, check=True)
        subprocess.run(("git", "config", "user.email", "teste@example.com"), cwd=self.root, check=True)
        subprocess.run(("git", "config", "user.name", "Teste"), cwd=self.root, check=True)
        (self.root / "README.md").write_text("base\n", encoding="utf-8")
        subprocess.run(("git", "add", "README.md"), cwd=self.root, check=True)
        subprocess.run(("git", "commit", "-q", "-m", "base"), cwd=self.root, check=True)
        self.previous_root = VALIDATOR.ROOT
        VALIDATOR.ROOT = self.root

    def tearDown(self):
        VALIDATOR.ROOT = self.previous_root
        self.temporary.cleanup()

    def write_note(self, status):
        path = self.root / "70 - Produções" / "Teste Temporário de Sobreposição.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            f"---\ntipo: estado-de-projeto\nstatus: {status}\n---\n\n"
            "Esta é a fonte canônica. A estrutura de 7 módulos/14 aulas governa "
            "o curso e somente neste chat ela pode ser revisada.\n",
            encoding="utf-8",
        )
        return path

    def test_rejects_new_active_rigidity_with_accented_path(self):
        self.write_note("vigente")
        errors = []
        VALIDATOR.validate_changed_documents(errors)
        self.assertTrue(any("fonte exclusiva" in error for error in errors))
        self.assertTrue(any("chat exclusivo" in error for error in errors))
        self.assertTrue(any("estrutura 7/14 governante" in error for error in errors))

    def test_allows_same_wording_in_historical_archive(self):
        self.write_note("acervo-historico-consultivo")
        errors = []
        VALIDATOR.validate_changed_documents(errors)
        self.assertEqual(errors, [])

    def test_ignores_legacy_term_hidden_by_descriptive_link_alias(self):
        path = self.root / "Estado e Continuidade.md"
        path.write_text(
            "---\ntipo: estado-de-projeto\nstatus: referencia-atual-revisavel\n---\n\n"
            "[[Pasta/Copy Canônica Antiga|Copy datada de referência]]\n",
            encoding="utf-8",
        )
        errors = []
        VALIDATOR.validate_changed_documents(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
