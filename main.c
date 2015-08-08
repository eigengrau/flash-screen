#include <gtk/gtk.h>
#include "cheese-flash.h"
#include "sound.h"

gboolean
timeout_quit(gpointer data)
{
  gtk_widget_destroy ( (GtkWidget *) data);
  return FALSE;
}

static void
doit (GtkApplication* app,
      gpointer        user_data)
{

  GtkWidget *window = gtk_application_window_new (app);
  GdkWindow *root_window = gdk_get_default_root_window ();
  GdkScreen *screen = gdk_window_get_screen (root_window);

  GdkRectangle rect;
  rect.height = gdk_screen_get_height (screen);
  rect.width = gdk_screen_get_width (screen);
  rect.x = 0;
  rect.y = 0;

  screenshot_play_sound_effect ("screen-capture", "Screenshot taken");

  CheeseFlash *flash = cheese_flash_new ();
  cheese_flash_fire (flash, &rect);
  g_object_unref (flash);

  g_timeout_add_seconds (1, timeout_quit, window);
}

int
main(int    argc,
     char **argv)
{
  GtkApplication *app;
  app = gtk_application_new (NULL, G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (doit), NULL);
  int status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);
  return status;
}
