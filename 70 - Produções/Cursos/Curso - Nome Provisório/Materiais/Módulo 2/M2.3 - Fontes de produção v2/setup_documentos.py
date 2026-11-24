def setup(d,size=11.5):
 s=d.sections[0];s.page_width=Cm(21);s.page_height=Cm(29.7)
 s.top_margin=Cm(1.65);s.bottom_margin=Cm(1.5);s.left_margin=Cm(1.9);s.right_margin=Cm(1.9)
 for name in ['Normal','Body Text']:
  st=d.styles[name];st.font.name='Inter';st.font.size=Pt(size);st.font.color.rgb=RGBColor.from_string('082A45');st.paragraph_format.line_spacing=1.12;st.paragraph_format.space_after=Pt(3)
 for name,sz in [('Title',26),('Heading 1',22),('Heading 2',19),('Heading 3',13)]:
  st=d.styles[name];st.font.name='EB Garamond';st.font.size=Pt(sz);st.font.color.rgb=RGBColor.from_string('173F52');st.paragraph_format.space_before=Pt(12);st.paragraph_format.space_after=Pt(8);st.paragraph_format.keep_with_next=True
 for st in d.styles:
  if st.type==1 and st.font.name:
   fonts=st.element.get_or_add_rPr().rFonts
   if fonts is not None:
    for a in list(fonts.attrib):
     if 'theme' in a.lower():del fonts.attrib[a]
    for a in ['ascii','hAnsi','eastAsia','cs']:fonts.set(qn('w:'+a),st.font.name)
  for node in list(st.element.xpath('.//w:pBdr')):node.getparent().remove(node)
 d.core_properties.author='Fabiano Deliberalli'

