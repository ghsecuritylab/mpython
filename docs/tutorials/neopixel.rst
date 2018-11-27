RGB LED
=====================

mPython掌控板载3颗ws2812灯珠，WS2812是一种集成了电流控制芯片的低功耗的RGB三色灯。采用特殊的单线通讯方式控制rgb灯颜色，使用简单。

板载RGB LED
----------

控制mPython掌控上的3颗RGB， 首先导入mpython模块::

    >>> from mpython import *
    
.. Note:: 导入mpython模块后，会为掌控创建一个NeoPixel对象rgb,控制板载的RGB只需对rgb对象操作。


设置每个像素点颜色::

    >>> rgb[0] = (255, 0, 0)  # 设置为红色，全亮度
    >>> rgb[1] = (0, 128, 0)  # 设定为绿色，半亮度
    >>> rgb[2] = (0, 0, 64)   # 设置为蓝色，四分之一亮度

然后使用 ``write()`` 将颜色输出到RGB灯::

    >>> rgb.write()

    
外部彩带
----------



如果需要使用外部彩带，要先创建一个neopixel对象,定义 ``pin`` 、``bpp`` 、 ``timeing`` 参数，然后才能通过该对象控制彩带上的LED。
更详细的使用方法，请查阅 :ref:`neopixel<neopixel>` 模块 。

.. image:: /images/tutorials/glamour.jpg
  :height: 300
  :width: 400

示例::

  import time
  import machine, neopixel
  np = neopixel.NeoPixel(machine.Pin(33), n=10,bpp=3,timing=1)

  def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
      for j in range(n):
        np[j] = (0, 0, 0)
      np[i % n] = (255, 255, 255)
      np.write()
      time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
      for j in range(n):
        np[j] = (0, 0, 128)
      if (i // n) % 2 == 0:
        np[i % n] = (0, 0, 0)
      else:
        np[n - 1 - (i % n)] = (0, 0, 0)
      np.write()
      time.sleep_ms(50)

    # fade in/out
    for i in range(0, 4 * 256, 8):
      for j in range(n):
        if (i // 256) % 2 == 0:
          val = i & 0xff
        else:
          val = 255 - (i & 0xff)
        np[j] = (val, 0, 0)
      np.write()

    # clear
    for i in range(n):
      np[i] = (0, 0, 0)
    np.write()
    
  while True:
    
    demo(np)
    
    


  
