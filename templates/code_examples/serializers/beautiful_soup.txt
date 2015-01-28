# -*- coding: utf-8 -*-

__author__ = 'Enrique Coslado'

import bs4

file_path = "nuevo-casino-valladolid-empleara-20150122104208.html"
html_doc = open(file_path).read()

soup = bs4.BeautifulSoup(html_doc)
print soup.prettify()

#<!DOCTYPE html>
#<html itemscope="" itemtype="http://schema.org/NewsArticle" lang="es" prefix="og: http://ogp.me/ns# article: http://ogp.me/ns/article#">
# <head>
#  <script src="/comun/js/2014/scfp-min.js" type="text/javascript">
#  </script>
#  <script type="text/javascript">
#   EV.init({authorizeUrl: "/ev_session_check/"});
#					EV.handleNewSession(function(result) {
#						if (!result.allowAccess) {
#							window.location.reload();
#						}
#					});
#  </script>
# </head>
# <body>
#  <img src="/evolok-ad-web/diag/cookie/54c8b89be4b09468a8aae3fc" style="display: none"/>
#  <title>
#   El nuevo casino de Valladolid empleará a 101 personas . elnortedecastilla.es
#  </title>
#  <meta content="El ?hagan juego, seסores? serב prבcticamente continuo. Desde las once de la maסana, con la apertura de una gran sala de mבquinas tragaperras con mבs de cuarenta aparatos de תltima generaciףn, juegos variados y una barra donde pedirse un trago para aliviar la tensiףn, y hasta las cuatro o seis de la madrugada ?dependiendo si es dםa de labor o festivo? con una larguםsima jornada vespertina donde se abrirב la oferta clבsica de ruleta, black jack o pףker, entre otras propuestas. El Ayuntamiento de Valladolid estב ultimando la tramitaciףn de las licencias ambiental y de obras para convertir el antiguo cine Roxy, en el nתmero 20 de la calle Marםa de Molina, en el Casino de Castilla y Leףn. Fuentes municipales confirman que la intenciףn es concluir este proceso en febrero con el objetivo de que los operarios puedan entrar de inmediato para iniciar unos trabajos, que se prolongarבn durante catorce meses. El presupuesto de la obra civil asciende a 812.833 euros, una partida a la que habrב que aסadir un amueblamiento que se quiere de primera calidad." name="Description"/>
# ...

# Print first title tag
print soup.title
#<title>El nuevo casino de Valladolid empleará a 101 personas . elnortedecastilla.es</title>

# Print title tag name
print soup.title.name
#title

# Print text in title tag
print soup.title.text
#El nuevo casino de Valladolid empleará a 101 personas . elnortedecastilla.es

# Print parent tag name
print soup.title.parent.name
# body

# Print first link
print soup.a
#<a class="fd gigya-registration-link" href="#">Registro</a

# Print first paragraph
print soup.p
#<p>
#<span class="gigya-user-first-name"></span>
#<span class="gigya-user-last-name"></span>
#</p>

# Get class from span in paragraph
print soup.p.span["class"]
['gigya-user-first-name']

# Get all links
print soup.find_all("a")
#[<a class="fd gigya-registration-link" href="#">Registro</a>, <a href="#"></a>,
#<a class="fd rg" href="http://www.elnortedecastilla.es/comun/html/2014/datos-personales.html">Mi cuenta</a>,
#<a href=""></a>, <a href="http://www.elnortedecastilla.es/hemeroteca">Hemeroteca</a>,
#<a href="http://oferplan.elnortedecastilla.es/planes-ofertas/valladolid" target="_blank">Oferplan</a>,
#<a href="http://entradas.elnortedecastilla.es/" target="_blank" title="Entradas">Entradas</a>]


# Get every element with id backcss
print soup.find_all(id="backcss")
#[<div id="backcss">
#<script>
#		var publiBackground = window['noticia_background_'+objectPublishId];
#		if (publiBackground!=undefined &&	publiBackground) {
#			ads.printAds({'position': 'backcss', 'id': 'backcss'});
#		}
#	</script>
#</div>]
