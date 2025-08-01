import streamlit as st

paginas = {
  'Páginas': [st.Page('paginas/pagina1.py',default = True)],
  'Exemplo': [st.Page('paginas/pagina2.py',default = False)]
}


# para navegar entre as páginas
pg = st.navigation(paginas)
pg.run()
