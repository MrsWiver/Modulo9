'use strict';
const form=document.getElementById('buscar-productos');
const list=document.getElementById('productos');
const status=document.getElementById('catalogo-estado');
const back=document.getElementById('anterior');
const next=document.getElementById('siguiente');
let pagina=1, consulta='', solicitud=0;
const dinero=new Intl.NumberFormat('es-CO',{style:'currency',currency:'COP',maximumFractionDigits:0});
async function cargar(){
 const intento=++solicitud;
 back.disabled=true;next.disabled=true;status.textContent='Consultando catálogo…';
 try{
  const res=await fetch('/api/productos?'+new URLSearchParams({q:consulta,pagina:String(pagina)}));
  const datos=await res.json();
  if(intento!==solicitud)return;
  if(!res.ok)throw new Error(datos.error||'No se pudo consultar el catálogo.');
  list.replaceChildren();
  for(const producto of datos.resultados){
   const article=document.createElement('article');article.className='product';
   const codigo=document.createElement('span');codigo.className='code';codigo.textContent=producto.codigo;
   const nombre=document.createElement('h3');nombre.textContent=producto.nombre;
   const precio=document.createElement('div');precio.className='price';precio.textContent=dinero.format(producto.precio_venta);
   const unidad=document.createElement('span');unidad.className='unit';unidad.textContent=(producto.unidad||'Unidad por confirmar')+' · '+producto.categoria;
   article.append(codigo,nombre,precio,unidad);list.append(article);
  }
  status.textContent=datos.total?`${datos.total} ${datos.total===1?"producto encontrado":"productos encontrados"}. Mostrando ${datos.resultados.length}.`:'No hay productos con esa búsqueda. Prueba un nombre o código diferente.';
  document.getElementById('pagina').textContent=`Página ${pagina} de ${Math.max(1,Math.ceil(datos.total/30))}`;
  back.disabled=pagina<=1;next.disabled=pagina*30>=datos.total;
 }catch(error){
  if(intento!==solicitud)return;
  list.replaceChildren();status.textContent=error.message||'No se pudo conectar. Vuelve a buscar para reintentar.';
 }
}
form.addEventListener('submit',event=>{event.preventDefault();consulta=document.getElementById('busqueda').value.trim();pagina=1;cargar();});
back.addEventListener('click',()=>{if(pagina>1){pagina--;cargar();}});
next.addEventListener('click',()=>{pagina++;cargar();});
cargar();
