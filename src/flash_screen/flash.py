"""A Gtk widget implementing a shutter flash & sound."""

import gi
gi.require_version('GSound', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, GSound


class Flash (Gtk.Window):
    """Make the screen flash."""

    def __init__(self,
                 duration=100,
                 fade=.95,
                 fps=120,
                 threshold=.95):
        """
        Args:
            duration (int): Hold-time for the flash, in ms. After this interval
                the flash begins to fade-out.
            fade (float): A factor by which the opacity is multiplied at each
                fade step.
            threshold (float): The opacity level at which the flash is
                considered finished.
        """

        super().__init__(Gtk.WindowType.POPUP)

        # Set geometry.
        screen = self.get_screen()
        width = screen.get_width()
        height = screen.get_height()
        self.resize(width, height)
        self.move(0, 0)

        # Make the window not look like a regular window.
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_keep_above(True)
        self.set_type_hint(Gdk.WindowTypeHint.NOTIFICATION)
        self.fullscreen()

        # Don’t take focus.
        self.set_accept_focus(False)
        self.set_focus_on_map(False)

        # Don’t cast a shadow.
        visual = screen.get_rgba_visual()
        if visual is None:
            visual = screen.get_system_visual()
        self.set_visual(visual)

        # Ready GSound.
        self.sound = GSound.Context()
        self.sound.init()

        # Set-up the flash.
        self._duration = duration
        self._fade = fade
        self._fps = fps
        self._threshold = threshold
        self._opacity = 1

        # Good to go.
        self.show_all()
        GObject.timeout_add(self._duration, self._begin_fade)
        self._fire_shutter_sound()

    def _fire_shutter_sound(self):

        self.sound.play_full({
            GSound.ATTR_EVENT_ID: 'screen-capture'
        })

    def on_draw(self, _wid, ctx):

        ctx.set_source_rgba(1, 1, 1, self._opacity)
        ctx.paint()

    def _begin_fade(self):

        GObject.timeout_add(1000 / self._fps, self._do_fade)

    def _do_fade(self):

        self._opacity *= self._fade
        self.queue_draw()

        if self._opacity <= self._threshold:
            self.hide()
            # Give the shutter sound time to finish.
            GObject.timeout_add(1000, Gtk.main_quit)
            return False
        else:
            return True
