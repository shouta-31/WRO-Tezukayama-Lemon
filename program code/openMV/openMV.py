import sensor, image, time, math
from pupremote import PUPRemoteSensor, OPENMV
p=PUPRemoteSensor(power=True)
p.add_channel('blob', to_hub_fmt='hhhhhhh')#h一つで整数一個を送るという意味。この場合7つ。
#現在の値はオレンジ
thresholds = [(0, 62, 19, 127, -128, 127)]#赤
thresholds2 = [(0, 100, -128, -24, -128, 127)]#緑
#色はLABで(Lmin,Lmax,Amin,Amax,Bmin,Bmax)の形式で指定
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False,gain_db=20)#,gain_db=17#光に対する明るさを調整
sensor.set_auto_whitebal(False)#,rgb_gain_db=(63.137, 60.206, 63.8122)
sensor.set_auto_exposure(False,exposure_us=15000)#,exposure_us=21450 #光を調整
print(sensor.get_exposure_us(),sensor.get_rgb_gain_db(),sensor.get_gain_db())
clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    largest_red_blob = []
    largest_red_blob_size = 0
    x=0
    y=0
    pixels=0
    p_x=0
    p_y=0
    p_pixels=0
    red_pixels=0
    largest_green_blob = []
    largest_green_blob_size = 0
    for blob in img.find_blobs(thresholds, pixels_threshold=100, area_threshold=100, merge=True):#赤
        img.draw_rectangle(blob.rect(),color=(255,0,0),thickness=3)
        img.draw_cross(blob.cx(), blob.cy(),color=(255,0,0),thickness=3)
        if blob.pixels() > largest_red_blob_size:
            largest_red_blob_size = blob.pixels()
            largest_red_blob = [blob.cx(), blob.cy(),blob.pixels()]
            x,y,pixels=largest_red_blob
            print(largest_red_blob)
    for blob in img.find_blobs(thresholds2, pixels_threshold=100, area_threshold=100, merge=True):#緑
        img.draw_rectangle(blob.rect(),color=(0,255,0),thickness=3)
        img.draw_cross(blob.cx(), blob.cy(),color=(0,255,0),thickness=3)
        if blob.pixels() > largest_green_blob_size:
            largest_green_blob_size = blob.pixels()
            largest_green_blob = [blob.cx(), blob.cy(),blob.pixels()]
            p_x,p_y,p_pixels=largest_green_blob
            print(largest_green_blob)

    print(x,y,pixels,p_x,p_y,p_pixels,red_pixels)
    p.update_channel('blob',x,y,pixels,p_x,p_y,p_pixels,red_pixels)
    state=p.process()
