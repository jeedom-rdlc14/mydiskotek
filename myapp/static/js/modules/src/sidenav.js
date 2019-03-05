(($) => {

  const MENU_WIDTH = 240;
  const SN_BREAKPOINT = 1440;
  const MENU_WIDTH_HALF = 2;
  const MENU_LEFT_MIN_BORDER = 0.3;
  const MENU_LEFT_MAX_BORDER = -0.5;
  const MENU_RIGHT_MIN_BORDER = -0.3;
  const MENU_RIGHT_MAX_BORDER = 0.5;
  const MENU_VELOCITY_OFFSET = 10;

  class SideNav {

    constructor(element, options) {

      this.defaults = {
        MENU_WIDTH,
        edge: 'left',
        closeOnClick: false,
        breakpoint: SN_BREAKPOINT
      };

      this.$element = element;
      this.options = this.assignOptions(options);

      this.menuOut = false;
      this.lastTouchVelocity = {
        x: {
          startPosition: 0,
          startTime: 0,
          endPosition: 0,
          endTime: 0
        }
      };

      this.$body = $('body');
      this.$menu = $(`#${this.$element.attr('data-activates')}`);
      this.$sidenavOverlay = $('#sidenav-overlay');
      this.$dragTarget = $('<div class="drag-target"></div>');
      this.$body.append(this.$dragTarget);

      this.init();
    }

    init() {

      this.setMenuWidth();
      this.setMenuTranslation();
      this.closeOnClick();
      this.openOnClick();
      this.bindTouchEvents();
    }

    bindTouchEvents() {

      this.$dragTarget.on('click', () => {

        this.removeMenu();
      });

      this.$dragTarget.on('touchstart', (e) => {

        this.lastTouchVelocity.x.startPosition = e.touches[0].clientX;
        this.lastTouchVelocity.x.startTime = Date.now();
      });
      this.$dragTarget.on('touchmove', this.touchmoveEventHandler.bind(this));
      this.$dragTarget.on('touchend', this.touchendEventHandler.bind(this));
    }

    touchmoveEventHandler(e) {

      if (e.type !== 'touchmove') {

        return;
      }

      const touch = e.touches[0];
      let touchX = touch.clientX;

      // calculate velocity every 20ms
      if (Date.now() - this.lastTouchVelocity.x.startTime > 20) {

        this.lastTouchVelocity.x.startPosition = touch.clientX;
        this.lastTouchVelocity.x.startTime = Date.now();
      }

      this.disableScrolling();

      const overlayExists = this.$sidenavOverlay.length !== 0;
      if (!overlayExists) {

        this.buildSidenavOverlay();
      }

      // Keep within boundaries
      if (this.options.edge === 'left') {

        if (touchX > this.options.MENU_WIDTH) {

          touchX = this.options.MENU_WIDTH;
        } else if (touchX < 0) {

          touchX = 0;
        }
      }

      this.translateSidenavX(touchX);
      this.updateOverlayOpacity(touchX);
    }

    panEventHandler(e) {

      if (e.gesture.pointerType !== 'touch') {

        return;
      }

      let touchX = e.gesture.center.x;

      this.disableScrolling();

      const overlayExists = this.$sidenavOverlay.length !== 0;
      if (!overlayExists) {

        this.buildSidenavOverlay();
      }

      // Keep within boundaries
      if (this.options.edge === 'left') {

        if (touchX > this.options.MENU_WIDTH) {

          touchX = this.options.MENU_WIDTH;
        } else if (touchX < 0) {

          touchX = 0;
        }
      }

      this.translateSidenavX(touchX);
      this.updateOverlayOpacity(touchX);
    }

    translateSidenavX(touchX) {

      if (this.options.edge === 'left') {

        const isRightDirection = touchX >= this.options.MENU_WIDTH / MENU_WIDTH_HALF;
        this.menuOut = isRightDirection;

        this.$menu.css('transform', `translateX(${touchX - this.options.MENU_WIDTH}px)`);
      } else {

        const isLeftDirection = touchX < window.innerWidth - this.options.MENU_WIDTH / MENU_WIDTH_HALF;
        this.menuOut = isLeftDirection;

        let rightPos = touchX - this.options.MENU_WIDTH / MENU_WIDTH_HALF;
        if (rightPos < 0) {
          rightPos = 0;
        }

        this.$menu.css('transform', `translateX(${rightPos}px)`);
      }
    }

    updateOverlayOpacity(touchX) {

      let overlayPercentage;
      if (this.options.edge === 'left') {

        overlayPercentage = touchX / this.options.MENU_WIDTH;
      } else {

        overlayPercentage = Math.abs((touchX - window.innerWidth) / this.options.MENU_WIDTH);
      }

      this.$sidenavOverlay.velocity({
        opacity: overlayPercentage
      }, {
        duration: 10,
        queue: false,
        easing: 'easeOutQuad'
      });
    }

    buildSidenavOverlay() {

      this.$sidenavOverlay = $('<div id="sidenav-overlay"></div>');
      this.$sidenavOverlay.css('opacity', 0)
        .on('click', () => {

          this.removeMenu();
        });

      this.$body.append(this.$sidenavOverlay);
    }

    disableScrolling() {

      const oldWidth = this.$body.innerWidth();
      this.$body.css('overflow', 'hidden');
      this.$body.width(oldWidth);
    }

    touchendEventHandler(e) {

      if (e.type !== 'touchend') {

        return;
      }

      const touch = e.changedTouches[0];

      this.lastTouchVelocity.x.endTime = Date.now();
      this.lastTouchVelocity.x.endPosition = touch.clientX;
      const velocityX = this.calculateTouchVelocityX();

      const touchX = touch.clientX;
      let leftPos = touchX - this.options.MENU_WIDTH;
      let rightPos = touchX - this.options.MENU_WIDTH / MENU_WIDTH_HALF;
      if (leftPos > 0) {
        leftPos = 0;
      }
      if (rightPos < 0) {
        rightPos = 0;
      }

      if (this.options.edge === 'left') {

        // If velocityX <= 0.3 then the user is flinging the menu closed so ignore this.menuOut
        if (this.menuOut && velocityX <= MENU_LEFT_MIN_BORDER || velocityX < MENU_LEFT_MAX_BORDER) {

          if (leftPos !== 0) {

            this.translateMenuX([0, leftPos], '300');
          }

          this.showSidenavOverlay();

        } else if (!this.menuOut || velocityX > MENU_LEFT_MIN_BORDER) {

          this.enableScrolling();
          this.translateMenuX([-1 * this.options.MENU_WIDTH - MENU_VELOCITY_OFFSET, leftPos], '200');
          this.hideSidenavOverlay();
        }

        this.$dragTarget.css({
          width: '10px',
          right: '',
          left: 0
        });
      } else if (this.menuOut && velocityX >= MENU_RIGHT_MIN_BORDER || velocityX > MENU_RIGHT_MAX_BORDER) {

        this.translateMenuX([0, rightPos], '300');
        this.showSidenavOverlay();

        this.$dragTarget.css({
          width: '50%',
          right: '',
          left: 0
        });
      } else if (!this.menuOut || velocityX < MENU_RIGHT_MIN_BORDER) {

        this.enableScrolling();
        this.translateMenuX([this.options.MENU_WIDTH + MENU_VELOCITY_OFFSET, rightPos], '200');
        this.hideSidenavOverlay();

        this.$dragTarget.css({
          width: '10px',
          right: 0,
          left: ''
        });
      }
    }

    calculateTouchVelocityX() {

      const distance = Math.abs(this.lastTouchVelocity.x.endPosition - this.lastTouchVelocity.x.startPosition);
      const time = Math.abs(this.lastTouchVelocity.x.endTime - this.lastTouchVelocity.x.startTime);

      return distance / time;
    }

    panendEventHandler(e) {

      if (e.gesture.pointerType !== 'touch') {

        return;
      }

      const velocityX = e.gesture.velocityX;
      const touchX = e.gesture.center.x;
      let leftPos = touchX - this.options.MENU_WIDTH;
      let rightPos = touchX - this.options.MENU_WIDTH / MENU_WIDTH_HALF;
      if (leftPos > 0) {
        leftPos = 0;
      }
      if (rightPos < 0) {
        rightPos = 0;
      }

      if (this.options.edge === 'left') {

        // If velocityX <= 0.3 then the user is flinging the menu closed so ignore this.menuOut
        if (this.menuOut && velocityX <= MENU_LEFT_MIN_BORDER || velocityX < MENU_LEFT_MAX_BORDER) {

          if (leftPos !== 0) {

            this.translateMenuX([0, leftPos], '300');
          }

          this.showSidenavOverlay();

        } else if (!this.menuOut || velocityX > MENU_LEFT_MIN_BORDER) {

          this.enableScrolling();
          this.translateMenuX([-1 * this.options.MENU_WIDTH - MENU_VELOCITY_OFFSET, leftPos], '200');
          this.hideSidenavOverlay();
        }

        this.$dragTarget.css({
          width: '10px',
          right: '',
          left: 0
        });
      } else if (this.menuOut && velocityX >= MENU_RIGHT_MIN_BORDER || velocityX > MENU_RIGHT_MAX_BORDER) {

        this.translateMenuX([0, rightPos], '300');
        this.showSidenavOverlay();

        this.$dragTarget.css({
          width: '50%',
          right: '',
          left: 0
        });
      } else if (!this.menuOut || velocityX < MENU_RIGHT_MIN_BORDER) {

        this.enableScrolling();
        this.translateMenuX([this.options.MENU_WIDTH + MENU_VELOCITY_OFFSET, rightPos], '200');
        this.hideSidenavOverlay();

        this.$dragTarget.css({
          width: '10px',
          right: 0,
          left: ''
        });
      }
    }

    translateMenuX(fromTo, duration) {

      this.$menu.velocity({
        translateX: fromTo
      }, {
        duration: typeof duration === 'string' ? Number(duration) : duration,
        queue: false,
        easing: 'easeOutQuad'
      });
    }

    hideSidenavOverlay() {

      this.$sidenavOverlay.velocity({
        opacity: 0
      }, {
        duration: 200,
        queue: false,
        easing: 'easeOutQuad',
        complete() {

          $(this).remove();
        }
      });

      this.$sidenavOverlay = $();
    }

    showSidenavOverlay() {

      this.$sidenavOverlay.velocity({
        opacity: 1
      }, {
        duration: 50,
        queue: false,
        easing: 'easeOutQuad'
      });
    }

    enableScrolling() {

      this.$body.css({
        overflow: '',
        width: ''
      });
    }

    openOnClick() {

      this.$element.on('click', (e) => {

        e.preventDefault();

        if (this.menuOut === true) {

          this.menuOut = false;
          this.removeMenu();
        } else {

          this.menuOut = true;
          this.$sidenavOverlay = $('<div id="sidenav-overlay"></div>');
          this.$body.append(this.$sidenavOverlay);

          let translateX = [];
          if (this.options.edge === 'left') {

            translateX = [0, -1 * this.options.MENU_WIDTH];
          } else {

            translateX = [0, this.options.MENU_WIDTH];
          }

          this.$menu.velocity({
            translateX
          }, {
            duration: 300,
            queue: false,
            easing: 'easeOutQuad'
          });

          this.$sidenavOverlay.on('click', () => {

            this.removeMenu();
          });
        }
      });
    }

    closeOnClick() {

      if (this.options.closeOnClick === true) {

        this.$menu.on('click', 'a:not(.collapsible-header)', () => {

          this.removeMenu();
        });
      }
    }

    setMenuTranslation() {

      if (this.options.edge === 'left') {

        this.$menu.css('transform', 'translateX(-100%)');
        this.$dragTarget.css({
          left: 0
        });
      } else {

        this.$menu.addClass('right-aligned').css('transform', 'translateX(100%)');
        this.$dragTarget.css({
          right: 0
        });
      }

      if (this.$menu.hasClass('fixed')) {

        if (window.innerWidth > this.options.breakpoint) {

          this.$menu.css('transform', 'translateX(0)');
        }

        $(window).resize(() => {

          if (window.innerWidth > this.options.breakpoint) {

            if (this.$sidenavOverlay.length) {

              this.removeMenu(true);
            } else {

              this.$menu.css('transform', 'translateX(0%)');
            }
          } else if (this.menuOut === false) {

            const xValue = this.options.edge === 'left' ? '-100' : '100';
            this.$menu.css('transform', `translateX(${xValue}%)`);
          }
        });
      }
    }

    setMenuWidth() {

      const $sidenavBg = $(`#${this.$menu.attr('id')}`).find('> .sidenav-bg');

      if (this.options.MENU_WIDTH !== MENU_WIDTH) {

        this.$menu.css('width', this.options.MENU_WIDTH);
        $sidenavBg.css('width', this.options.MENU_WIDTH);
      }
    }

    assignOptions(newOptions) {

      return $.extend({}, this.defaults, newOptions);
    }

    removeMenu(restoreMenu) {

      this.$body.css({
        overflow: '',
        width: ''
      });

      this.$menu.velocity({
        translateX: this.options.edge === 'left' ? '-100%' : '100%'
      }, {
        duration: 200,
        queue: false,
        easing: 'easeOutCubic',
        complete: () => {
          if (restoreMenu === true) {
            this.$menu.removeAttr('style');
            this.$menu.css('width', this.options.MENU_WIDTH);
          }
        }
      });

      this.hideSidenavOverlay();
    }

    show() {

      this.trigger('click');
    }

    hide() {

      this.trigger('click');
    }

  }

  $.fn.sideNav = function (options) {
    return this.each(function () {
      new SideNav($(this), options);
    });
  };

})(jQuery);

$(function() {
  $("#toggle").click(function() {
    if ($("#slide-out").hasClass('slim')) {
      $("#slide-out").removeClass('slim');
      $(".sv-slim-icon").removeClass('fa-angle-double-right').addClass('fa-angle-double-left');
    } else {
      $("#slide-out").addClass('slim');
      $(".sv-slim-icon").removeClass('fa-angle-double-left').addClass('fa-angle-double-right');
    }
  });
});
