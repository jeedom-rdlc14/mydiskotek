 $.fn.mdbAutocomplete = function (options) {

   const defaults = {
     data: {},
     dataColor: '',
     xColor: '',
     xBlurColor: '#ced4da',
     inputFocus: '1px solid #4285f4',
     inputBlur: '1px solid #ced4da',
     inputFocusShadow: '0 1px 0 0 #4285f4',
     inputBlurShadow: ''
   };

   const ENTER_CHAR_CODE = 13;

   options = $.extend(defaults, options);

   return this.each((index, ev) => {

     const $input = $(ev);
     let $autocomplete;
     const data = options.data;
     const dataColor = options.dataColor;
     const xColor = options.xColor;
     const xBlurColor = options.xBlurColor;
     const inputFocus = options.inputFocus;
     const inputBlur = options.inputBlur;
     const inputFocusShadow = options.inputFocusShadow;
     const inputBlurShadow = options.inputBlurShadow;

     if (Object.keys(data).length) {

       $autocomplete = $('<ul class="mdb-autocomplete-wrap"></ul>');
       $autocomplete.insertAfter($input);
     }

     $input.on('focus', () => {

       $input.css('border-bottom', inputFocus);
       $input.css('box-shadow', inputFocusShadow);
     });

     $input.on('blur', () => {

       $input.css('border-bottom', inputBlur);
       $input.css('box-shadow', inputBlurShadow);
     });

     $input.on('keyup', e => {

       const $inputValue = $input.val();

       $autocomplete.empty();

       if ($inputValue.length) {

         for (const item in data) {

           if (data[item].toLowerCase().indexOf($inputValue.toLowerCase()) !== -1) {

             const option = $(`<li>${data[item]}</li>`);

             $autocomplete.append(option);
           }
         }
       }

       if (e.which === ENTER_CHAR_CODE) {

         $autocomplete.children(':first').trigger('click');
         $autocomplete.empty();
       }

       if ($inputValue.length === 0) {

         $input.parent().find('.mdb-autocomplete-clear').css('visibility', 'hidden');
       } else {

         $input.parent().find('.mdb-autocomplete-clear').css('visibility', 'visible');
       }

       $('.mdb-autocomplete-wrap li').css('color', dataColor);
     });

     $autocomplete.on('click', 'li', e => {

       $input.val($(e.target).text());

       $autocomplete.empty();
     });

     $('.mdb-autocomplete-clear').on('click', e => {

       e.preventDefault();

       let $this = $(e.currentTarget);

       $this.parent().find('.mdb-autocomplete').val('');
       $this.css('visibility', 'hidden');
       $autocomplete.empty();
       $this.parent().find('label').removeClass('active');
     });

     $('.mdb-autocomplete').on('click keyup', e => {

       e.preventDefault();
       $(e.target).parent().find('.mdb-autocomplete-clear').find('svg').css('fill', xColor);
     });

     $('.mdb-autocomplete').on('blur', e => {

       e.preventDefault();
       $(e.target).parent().find('.mdb-autocomplete-clear').find('svg').css('fill', xBlurColor);
     });
   });
 };

 $.fn.mdb_autocomplete = $.fn.mdbAutocomplete;
