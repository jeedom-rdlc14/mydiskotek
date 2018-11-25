/*!
 * mydiskotek.js 0.1.0
 * mes fonctions javascript pour l'appli mydiskotek
 * Copyright 2018 Rdlc_Dev
 */

/*!
 * fonction de recherche des artistes ou albums
 */

   var albums = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('title'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: '/static/data/albumsList.json'
    });
        
    var artists = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: '/static/data/artistsList.json'
    });
    
    
    $('#multi-dataset .typeahead').typeahead({
        minLength: 1,
        hint: true,
        highlight: true
    },
    {
        name: 'artists-names',
        display: 'name',
        source: artists,
        templates: {
            header: '<p class="h5">Artistes</p>'
        }
    },
    {
        name: 'albums-titles',
        display: 'title',
        source: albums,
        templates: {
          header: '<p class="h5">Albums</p>'
        }
    }).on('typeahead:selected', function (e, datum) {
        if (datum.name != null) {
            console.log(datum.name)
            location.href='{{serverURL}}/artist/' + datum.name
        };
        
        if (datum.title != null){
            console.log(datum.title)
            location.href='{{serverURL}}/title/' + datum.title
        };
    });

/*!
 * Recherche Artistes et Albums
 */

var albums = new Bloodhound({
 datumTokenizer: Bloodhound.tokenizers.obj.whitespace('title'),
 queryTokenizer: Bloodhound.tokenizers.whitespace,
 prefetch: '/static/data/json/albumsList.json'
});
 
var artists = new Bloodhound({
 datumTokenizer: Bloodhound.tokenizers.obj.whitespace('name'),
 queryTokenizer: Bloodhound.tokenizers.whitespace,
 prefetch: '/static/data/json/artistsList.json'
});


$('#multi-dataset .typeahead').typeahead({
 minLength: 1,
 hint: true,
 highlight: true
},
{
 name: 'artists-names',
 display: 'name',
 source: artists,
 templates: {
     header: '<p class="h5">Artistes</p>'
 }
},
{
 name: 'albums-titles',
 display: 'title',
 source: albums,
 templates: {
   header: '<p class="h5">Albums</p>'
 }
}).on('typeahead:selected', function (e, datum) {
 if (datum.name != null) {
     console.log(datum.name)
     location.href='{{serverURL}}/artist/' + datum.name
 };

 if (datum.title != null){
     console.log(datum.title)
     location.href='{{serverURL}}/title/' + datum.title
 };
});

/*!
 *  gestion des boutons radio (support et genre)
 */

// get value of selected 'formatRadio' and 'genreRadio' radio buttons in 'listsForm'
function getRadioVal(formulaire, radio) {
 
 var boutons = document.getElementsByName(radio);
 var valeur = '';
 for(var i = 0; i < boutons.length; i++){
     if(boutons[i].checked){
         valeur = boutons[i].value;
     }
 }
 
 return valeur;
}

function listsCollection() {
 var formatVal = getRadioVal('listsForm', 'formatRadio');
 var genreVal = getRadioVal('listsForm', 'genreRadio');
 
 switch(formatVal) {
      case('Tout'):
         if (genreVal === '') {
             document.location.href='{{serverURL}}/list/';
         } else {
             document.location.href='{{serverURL}}/categorie/' + genreVal;
         }
         break;
                                     
     default:
         if (genreVal === '') {
             document.location.href='{{serverURL}}/' + formatVal +'/';
         } else {
             document.location.href='{{serverURL}}/list/' + formatVal +'/' + genreVal + '/';
         }
 }
}

function printCollections() {
 var formatVal = getRadioVal('listsForm', 'formatRadio');
 var genreVal = getRadioVal('listsForm', 'genreRadio');
 
 switch(formatVal) {
      case('Tout'):
         alert("Pas d'impression possible pour la collection entière!");
         break;
                            
     default:
         if (genreVal === '') {
             var valGenre = 'undefined';
             document.location.href='{{serverURL}}/imprim/' + formatVal +'/' + valGenre + '/';
         } else {
             document.location.href='{{serverURL}}/imprim/' + formatVal +'/' + genreVal + '/';
         }
         
 }
}


