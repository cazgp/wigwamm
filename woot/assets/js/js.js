
// MAKE CLICKS FAST!
window.addEventListener('load', function() {
    new FastClick(document.body);
}, false);


$(window).load(function(){

/****************************************************
 * HANDLE INPUT CHANGES SO SUMMARY IS AUTOMATICALLY
 * KEPT IN SYNC
 * **************************************************/
  $('.question input').change(function(e) {
    var target = e.currentTarget;
    var name = target.name;
    var value;
    // If dealing with radio, we can get the value by the label
    if(target.type === 'radio') {
      var label = target.labels[0];
      value = label.innerText || label.textContent;
      console.log("radio")
    }
    var summary = $('.' + name + '-summary span');
    summary.text(value);
  });

  // Set the hidden date input when the radio buttons change
  $("input[name='move-in-date']").change(function(e) {
    $('#id_move_in_date').val(e.currentTarget.id);
  });
  

  // FOCUS THE CURSOR IN THE POSTCODE INPUT ON PAGE LOAD
  //$('.postcode').focus();
  // FOCUS THE CURSOR IN THE ADDRESS INPUT ON PAGE LOAD
  $('input.address').focus().change(function(e) {
    console.log(e.currentTarget);
    $('.address-summary span').text(e.currentTarget.value);
  });

  $('#id_council_borough').change(function(e) {
    $('.council_borough-summary').text(e.currentTarget.value);
  });
  $('#id_epc_code').change(function(e) {
    $('.epc_code-summary').text(e.currentTarget.value);
  });

  //GO TO NEXT QUESTION ON CLICK WITH 300MS DELAY SO YOU KNOW WHAT YOU'VE CLICKED
  $('li:not(.requires-next-button) input:radio, .addresses li a').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li:not(.disabled), :has(li)').first();
      $('body').delay(200).animate({scrollTop:nextdiv.offset().top},400);    
  });

  // GO TO NEXT QUESTION ON CLICK WITH NO DELAY
  $('.next, .skip').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li:not(.disabled), :has(li)').first();
      $('body').animate({scrollTop:nextdiv.offset().top},400);    
  });
  
  
  // BACK BUTTON
  $('.back').bind('touchend, click', function(e){
      prevdiv = $(this).closest('.question').prevAll('li:not(.disabled), :has(li)').first();
      $('body').animate({scrollTop:prevdiv.offset().top},400);
  });
  
  
  // ADDRESS CHOOSING
  //$('.addresses li a').bind('click', function(e){
      //$('.addresses li a').removeClass('selected');
      //$(this).addClass('selected');
  //});
  
  
  // MOVE IN DATE
  $('.move-in input:radio').bind('change', function(e){
      $('.move-in .next-bar').removeClass('disabled');
      $('.move-in .grid-container').addClass('chosen');
  });
  
  
  // FLOOR PICKER
  $('.floor input:radio').bind('change', function(e){
      $('.floor .next-bar').removeClass('disabled');
      $('.floor .grid-container').addClass('chosen');
  });
  
  // Keypad bindings
  tobind = ['price', 'bedrooms', 'bathrooms', 'agent-fee'];
  for(var b in tobind) {
    bind = tobind[b];
    make_binding(bind, '.'+bind+' a.keypad-button', '.'+bind+'-value');
  }

  // Event handler for when key is pressed
  function make_binding(b, binder, disp) {
    $(binder).bind('touchend, click', function(e) {
      var target  = e.currentTarget;
      var display = $(disp);
      var currentValue = display.val();
      var newValue;
      if(/backspace/.test(target.className)) {
        newValue = currentValue.slice(0, -1);
      }
      else {
        var value = e.currentTarget.innerText || e.currentTarget.textContent;
        newValue = currentValue + value;
      }
      // Update the summary and the span
      display.val(newValue);
      b = b.replace('-', '_');
      console.log(b);
      $('.' + b + '-summary span').html(newValue);
    });
  }

  // PHOTO SKIP TO NEXT
  $('.living-room-photo .no-photo, .kitchen-photo .no-photo, .exterior-photo .no-photo, .floorplan-photo .no-photo').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li:not(.disabled), :has(li)').first();
      $('body').animate({scrollTop:nextdiv.offset().top},400);    
  });
  
  // PHOTO SKIP TO NEXT SECTION (FOR BEDROOMS/BATHROOMS/ADDITIONAL WHEN ALL HAVE BEEN ENTERED ALREADY)
  $('.bedroom-photo .no-photo').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li.bathroom-photo').first();
      $('body').animate({scrollTop:nextdiv.offset().top},800);   
  }); 
  
  $('.bathroom-photo .no-photo').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li.additional-room-1-photo').first();
      $('body').animate({scrollTop:nextdiv.offset().top},800);    
  }); 
  
  $('.additional-room-photo .no-photo').bind('touchend, click', function(e){
      nextdiv = $(this).closest('.question').nextAll('li.exterior-photo').first();
      $('body').animate({scrollTop:nextdiv.offset().top},800);    
  }); 
  
  
  // EPC
  $('.no-epc').bind('click', function(e){
      $('.epc.question input, .epc.question h4 a').addClass('disabled');
      $('.epc.question .epc-requested').removeClass('disabled');
      return false;
  });
  
  $('.epc-requested a').bind('click', function(e){
      $('.epc.question input, .epc.question h4 a').removeClass('disabled');
      $('.epc.question .epc-requested').addClass('disabled');
      return false;
  });
  
  // ADD OR REMOVE LOGIN/SIGNUP FROM LISTING FLOW DEPENDING ON WHETHER THEY HAVE AN ACCOUNT OR NOT  
  $('.wigwamm-login-or-signup input').bind('touchend click', function(e){
    if($('#wigwamm-login-check').is(":checked")) {
        $('li.wigwamm-signup').addClass('disabled');
        $('li.wigwamm-login').removeClass('disabled');
    } else {
        $('li.wigwamm-login').addClass('disabled');
        $('li.wigwamm-signup').removeClass('disabled');
    }
  });
  
  // ADD 'SKIP TO SUMMARY' BUTTON WHEN AN EDIT IS MADE
  $('.summary .edit').bind('click', function(e){
      $('.skip-to-summary').removeClass('disabled');
  });
  
  // SCROLL BACK TO SUMMARY WHEN 'SKIP TO SUMMARY' BUTTON IS CLICKED
  $('.skip-to-summary').bind('click', function(e){
      $('body').animate({scrollTop:$('.summary.question').offset().top},800);   
  });
  
  // WHEN AN EDIT BUTTON IS CLICKED, SCROLL TO RELEVANT QUESTION DIV
  $('.summary .edit').bind('click', function(e) {
    var questionName = e.currentTarget.nextElementSibling.className.replace('-summary', '');
    $('body').animate({scrollTop:$('.' + questionName + '.question').offset().top},800);   
  });
 
  /* PROGRESS BAR IS A BIT GLITCHY, COMMENTING OUT FOR NOW
  
  $('li.question.postcode a').bind('touchend click', function(e){
      $(".progress-bar").width('3%');
  });
  
  $('li.question.portals a.next').bind('touchend click', function(e){
      $(".progress-bar").width('6%');
  });
  
  $('li.question.move-in a.next').bind('touchend click', function(e){
      $(".progress-bar").width('9%');
  });
  
  $('li.question.price a.next').bind('touchend click', function(e){
      $(".progress-bar").width('12%');
  });
  
  $('li.question.photos a.next').bind('touchend click', function(e){
      $(".progress-bar").width('15%');
  });
  
  $('li.question.floor a.next').bind('touchend click', function(e){
      $(".progress-bar").width('18%');
  });
  
  $('li.question.lift :input').bind('touchend click', function(e){
      $(".progress-bar").width('21%');
  });
  
  $('li.question.kitchen :input, li.question.kitchen a').bind('touchend click', function(e){
      $(".progress-bar").width('24%');
  });
  
  $('li.question.front-garden :input, li.question.front-garden a').bind('touchend click', function(e){
      $(".progress-bar").width('27%');
  });
  
  $('li.question.rear-garden :input, li.question.rear-garden a').bind('touchend click', function(e){
      $(".progress-bar").width('30%');
  });
  
  $('li.question.on-street-parking :input, li.question.on-street-parking a').bind('touchend click', function(e){
      $(".progress-bar").width('33%');
  });
  
  $('li.question.off-street-parking :input, li.question.off-street-parking a').bind('touchend click', function(e){
      $(".progress-bar").width('36%');
  });
  
  $('li.question.pets :input, li.question.pets a').bind('touchend click', function(e){
      $(".progress-bar").width('39%');
  });
  
  $('li.question.heating :input, li.question.heating a').bind('touchend click', function(e){
      $(".progress-bar").width('42%');
  });
  
  $('li.question.glazing :input, li.question.glazing a').bind('touchend click', function(e){
      $(".progress-bar").width('45%');
  });
  
  $('li.question.window-frames :input, li.question.window-frames a').bind('touchend click', function(e){
      $(".progress-bar").width('48%');
  });
  
  $('li.question.furnished :input, li.question.furnished a').bind('touchend click', function(e){
      $(".progress-bar").width('51%');
  });
  
  $('li.question.decorated :input, li.question.decorated a').bind('touchend click', function(e){
      $(".progress-bar").width('54%');
  });
  
  $('li.question.deposit :input, li.question.deposit a').bind('touchend click', function(e){
      $(".progress-bar").width('57%');
  });
  
  $('li.question.agreement-term :input, li.question.agreement-term a').bind('touchend click', function(e){
      $(".progress-bar").width('60%');
  });
  
  $('li.question.water-bills :input, li.question.water-bills a').bind('touchend click', function(e){
      $(".progress-bar").width('64%');
  });
  
  $('li.question.council-tax :input, li.question.council-tax a').bind('touchend click', function(e){
      $(".progress-bar").width('68%');
  });
  
  $('li.question.energy-bills :input, li.question.energy-bills a').bind('touchend click', function(e){
      $(".progress-bar").width('72%');
  });
  
  $('li.question.telephone-bills :input, li.question.telephone-bills a').bind('touchend click', function(e){
      $(".progress-bar").width('76%');
  });
  
  $('li.question.broadband :input, li.question.broadband a').bind('touchend click', function(e){
      $(".progress-bar").width('80%');
  });
  
  $('li.question.council-tax-borough :input, li.question.council-tax-borough a').bind('touchend click', function(e){
      $(".progress-bar").width('84%');
  });
  
  $('li.question.council-tax-band :input, li.question.council-tax-band a').bind('touchend click', function(e){
      $(".progress-bar").width('88%');
  });
  
  $('li.question.agent-fee :input, li.question.agent-fee a').bind('touchend click', function(e){
      $(".progress-bar").width('92%');
  });
  
  $('li.question.managed-by :input, li.question.managed-by a').bind('touchend click', function(e){
      $(".progress-bar").width('96%');
  });
  
  $('li.question.epc :input, li.question.epc a').bind('touchend click', function(e){
      $(".progress-bar").width('100%');
  });
  
  */
  
});

  
  // PHOTO UPLOAD - PLACE SELECTED IMAGE IN PREVIEW AREA
  function readURL(input) {
      if (input.files && input.files[0]) {
          var reader = new FileReader();
          var preview = $(input).parent().find('img');
          
          reader.onload = function (e) {
              preview.attr('src', e.target.result).width('100%');
          };
          reader.readAsDataURL(input.files[0]);
      }
  } 
  
  // FAKE THE CLICKING OF THE UPLOAD INPUT FROM THE 'TAKE PHOTO' AND 'X' BUTTONS
  $(window).load(function () {
      $('.take-photo').bind('touchend, click', function(e){
          $(this).closest('.preview').addClass('added');
          $(this).closest('.preview').children('.take-photo-input').click().addClass('added');
          samediv = $(this).closest('.question');
          $('body').delay(200).animate({scrollTop:samediv.offset().top},400);
          return true;
      });
  });
  
  
  

/****************************************************
STOP EVERYTHING BEING SCROLLED EXCEPT FOR .scrollable
****************************************************/

//uses document because document will be topmost level in bubbling
$(document).on('touchmove',function(e){
  e.preventDefault();
});
//uses body because jquery on events are called off of the element they are
//added to, so bubbling would not work if we used document instead.
$('body').on('touchstart','.scrollable',function(e) {
  if (e.currentTarget.scrollTop === 0) {
    e.currentTarget.scrollTop = 1;
  } else if (e.currentTarget.scrollHeight === e.currentTarget.scrollTop + e.currentTarget.offsetHeight) {
    e.currentTarget.scrollTop -= 1;
  }
});
//prevents preventDefault from being called on document if it sees a card div
$('body').on('touchmove','.scrollable',function(e) {
  e.stopPropagation();
});



// ADDING .INTERNAL CLASS TO AN <a> WILL STOP IT FROM OPENING SAFARI
$( document ).on(
  "click",
  "a.internal",
  function( event ){
   
  // Stop the default behavior of the browser, which
  // is to change the URL of the page.
  event.preventDefault();
   
  // Manually change the location of the page to stay in
  // "Standalone" mode and change the URL at the same time.
  location.href = $( event.target ).attr( "href" );
   
  }
);
