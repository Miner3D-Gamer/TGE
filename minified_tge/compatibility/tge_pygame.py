import os,pygame
from..tbe import pass_func
def update_screen(clock,fps=0):pygame.display.update();clock.tick(fps)
def render_text(screen,text,font_name,size,color,position):font=pygame.font.SysFont(font_name,size);rendered_text=font.render(text,True,color);screen.blit(rendered_text,position)
def load_images_from_directory(directory_path):
 supported_extensions=['.png','.jpg','.jpeg','.gif','.bmp','.tga','.lbm','.pbm','.ppm','.svg','.tiff','.webp','.xbm','.xpm','.tif'];files=0
 for(root,_,file_names)in os.walk(directory_path):
  for file_name in file_names:
   file_path=os.path.join(root,file_name)
   if os.path.splitext(file_path)[1]not in supported_extensions:continue
   globals()[file_name]=pygame.image.load(file_path);files+=1
 return files
def handle_events(quit_callback=exit,key_callback=pass_func,mouse_button_callback=pass_func,misc_callback=pass_func):
 for event in pygame.event.get():
  if event.type==pygame.QUIT:quit_callback()
  elif event.type==pygame.KEYDOWN:key_callback(event.key)
  elif event.type==pygame.MOUSEBUTTONDOWN:mouse_button_callback(event.button)
  else:misc_callback(event)
def check_collision(*rects):
 for i in range(len(rects)):
  for j in range(i+1,len(rects)):
   if rects[i].colliderect(rects[j]):return True
 return False
def check_collision_with_all(*rects):
 for i in range(len(rects)):
  for j in range(len(rects)):
   if not rects[i].colliderect(rects[j]):return False
 return True
def pygame_exit():pygame.quit()
def background_color(window,color):window.fill(color)
def draw_texture_at(surface,texture,position):surface.blit(texture,position)
def exit():pygame.quit();quit()