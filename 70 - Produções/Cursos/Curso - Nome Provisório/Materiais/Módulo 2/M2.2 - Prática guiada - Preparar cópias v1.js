async ({presentation}) => {
  const fs = await import('node:fs/promises');
  const indices = [0, 13, 14, 15, 16, 17, 18];
  const templates = indices.map(i => ({sourceIndex:i, material:presentation.slides.getItem(i).copy().materialize()}));
  await fs.writeFile('/tmp/tsh-m22-slide-materials.json', JSON.stringify(templates));
  return {templates:templates.length};
}
