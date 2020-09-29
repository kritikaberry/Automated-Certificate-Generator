import numpy as np
import pandas as pd
from PIL import ImageDraw,ImageFont,ImageColor,Image 
df=pd.read_excel(r"C:\Users\Kritika\Desktop\webdev\Automated Certificate Generator\Book1.xlsx")
print(df)
cert_names=df['Name'].tolist()
for name in cert_names:
    cert_t=Image.open(r"C:\Users\Kritika\Desktop\Sample-Certificate.png",mode="r")
    cert_temp=cert_t.convert("RGB")
    draw=ImageDraw.Draw(cert_temp)
    coord=(1026,861)
    font=ImageFont.truetype(r"C:\WINDOWS\FONTS\ARIAL.ttf",150)
    color_pix=(0,137,209)
    draw.text(coord,name,fill=color_pix,font=font)
    cert_temp.save(name+".pdf")
print("Done")

