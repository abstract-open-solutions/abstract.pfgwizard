$(document).ready(function(){

  if(typeof pfg_wizard != undefined) {
    if(pfg_wizard.on && !$('body').hasClass('template-base_edit')) {
      make_tabs('#pfg-fieldwrapper');
    }
  }

});


var make_tabs = function make_tabs(wrapper_sel) {
  // render form fieldsets as tabs
  var $wrapper = $(wrapper_sel);
  var nav = document.createElement('ul');
  nav.className = 'tab-nav';
  $('fieldset legend', $wrapper).each( function(){
    var legend = this,
        fieldset = this.parentNode;
        li =  document.createElement('li'),
        tab = document.createElement('a');
    tab.id = 'tab-' + this.getAttribute('for');
    tab.href = '#' + this.getAttribute('for');
    tab.innerHTML = this.innerHTML;
    if ($(fieldset).find('.fieldErrorBox').html()){
      tab.className = 'error';
    }
    li.appendChild(tab);
    nav.appendChild(li);
  });
  $wrapper.before(nav);

  $("ul.tab-nav").tabs(wrapper_sel + " > fieldset");

  // prev next buttons
  var bottom_nav = document.createElement('div');
  bottom_nav.className = 'prev-next-nav';
  prev = document.createElement('a');
  prev.href = '#';
  prev.className = 'prev';
  prev.innerHTML = 'prev';
  next = document.createElement('a');
  next.href = '#';
  next.className = 'next';
  next.innerHTML = 'next';
  bottom_nav.appendChild(prev);
  bottom_nav.appendChild(next);
  // append to wrapper and hook actions
  $wrapper.after(bottom_nav);
  api = $("ul.tab-nav").data("tabs");
  $('a.prev').click(function(){
    api.prev();
    return false;
  })
  $('a.next').click(function(){
    api.next();
    return false;
  })
}

