# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:59:23 2020

@author: user1
"""

# Tkinterライブラリのインポート
import tkinter as tk
import time
import os

from selenium import webdriver #Selenium Webdriverをインポートして
from webdriver_manager.chrome import ChromeDriverManager

from tkinter import messagebox

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.chrome.service import Service

# 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# コンソールの1行目の空行を非表示
os.environ['WDM_PRINT_FIRST_LINE'] = 'False'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://live.fc2.com/')

class Application(tk.Frame):
    
    groval_X = ""
    groval_Y = ""
    
    def __init__(self, master = None):
        super().__init__(master)
                
        # Scale（オプションをいくつか設定）
        self.scale_var_X = tk.DoubleVar()
        scaleX = tk.Scale( self.master, 
                    variable = self.scale_var_X, 
                    command = self.slider_scrollX,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = -150,            # 最小値（開始の値）
                    to = 150,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleX.place(x=0, y=150)
        '''scaleX.pack()'''
        scaleX.set(0)
        
        
        # Scale（オプションをいくつか設定）
        self.scale_var_Y = tk.DoubleVar()
        scaleY = tk.Scale( self.master, 
                    variable = self.scale_var_Y, 
                    command = self.slider_scrollY,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 300,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 20,      # スライダー（つまみ）の幅
                    from_ = -150,            # 最小値（開始の値）
                    to = 150,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=50         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleY.place(x=0, y=200)
        scaleY.set(0)
 
        # ラジオボックス
        self.v1 = tk.IntVar(value=1)
        self.radioBtn1 = tk.Radiobutton(value=1, variable=self.v1, command=self.change_state)
        self.radioBtn1.place(x=5, y=35)

        # テキストボックス
        self.txt = tk.Entry(width=30)
        self.txt.place(x=30, y=35)
        
        self.radioBtn2 = tk.Radiobutton(value=2, variable=self.v1, command=self.change_state)
        self.radioBtn2.place(x=250, y=35)
        
        # ギフト機能        
        self.gift_box = tk.StringVar()
        self.gift_val = ("いいね", "ハート", "キッス", "花火", "シャンパン")
        self.gift_box = tk.Spinbox(
            self.master,
            from_=0,
            to=4,
            state=tk.DISABLED,
            value= self.gift_val
        )
        self.gift_box.place(x=280, y=35)
        
        # ラベル
        self.tip_lbl = tk.Label(text='チップする値を入力してください', foreground='#faf0e6', background='#778899')
        self.tip_lbl.place(x=10, y=10)
        
        self.tip_lbl = tk.Label(text='ギフトを選んでください', foreground='#faf0e6', background='#778899')
        self.tip_lbl.place(x=250, y=10)
        
        self.lotate_lbl = tk.Label(text='連投する回数を決めてください', foreground='#faf0e6', background='#778899')
        self.lotate_lbl.place(x=10, y=60)
        
        self.lotate_lbl = tk.Label(text='連投間隔を決めてください', foreground='#faf0e6', background='#778899')
        self.lotate_lbl.place(x=10, y=110)
        
        self.tip_lbl = tk.Label(text='チップ画面調整用', foreground='#faf0e6', background='#778899')
        self.tip_lbl.place(x=100, y=270)
        
        self.tip_lbl = tk.Label(text='連投ボタン', foreground='#faf0e6', background='#778899')
        self.tip_lbl.place(x=10, y=270)
        
        # SpinBoxを作成
        self.sptxt = tk.IntVar()
        self.sptxt = tk.Spinbox(self.master, from_=1, to=50, increment=1, state='readonly')
        self.sptxt.grid(row=1,column=1)
        self.sptxt.grid_configure(padx=10, pady=85)
        
        # Startボタン作成
        self.start = tk.Button(root, text="スタート", command = self.btn_click) # ボタンの設定(text=ボタンに表示するテキスト)
        self.start.place(x=13,y=300) #ボタンを配置する位置の設定
        
        # チップ画面調整用ボタン作成
        self.tip_frame_window = tk.Button(root, text="Pボタン", command = self.tipBtn_click) # ボタンの設定(text=ボタンに表示するテキスト)
        self.tip_frame_window.place(x=125,y=300) #ボタンを配置する位置の設定
        
        # タブ切り替えボタン作成
        self.tab_change = tk.Label(text='複数タブ切り替え用', foreground='#faf0e6', background='#778899')
        self.tab_change.place(x=200, y=270)
        
        self.change_txt = tk.IntVar()
        self.change_txt = tk.Spinbox(
            self.master,
            from_=1,
            to=10,
            increment=1,
            state='readonly'
        )
        self.change_txt.place(x=205, y=305)
        
        self.change_btn = tk.Button(root, text="切り替え", command = self.change_click) # ボタンの設定(text=ボタンに表示するテキスト)
        self.change_btn.place(x=355,y=300) #ボタンを配置する位置の設定
        
        # 連投間隔機能        
        self.tip_time = tk.IntVar()
        self.val = (0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0)
        self.tip_time = tk.Spinbox(
            self.master,
            from_=0,
            to=10,
            state='readonly',
            value= self.val
        )
        self.tip_time.place(x=10, y=135)
        
        # チェックボタン
        
        # ウィジェット変数の作成
        self.check_v = tk.BooleanVar()
        self.chk = tk.Checkbutton(
            root, 
            text='高速化',
            variable=self.check_v,
            onvalue=True,
            offvalue=False
            )
        self.chk.place(x=150, y=132)
        
    # 状態の変更
    def change_state(self, event=None):
        # チェックされているラジオボタンを取得
        checked = self.v1.get()
        print("ラジオ:"+str(checked))
        
        if checked == 1:
            self.txt.configure(state="normal")
            self.gift_box.configure(state="disabled")
            
        elif checked == 2:
            self.txt.configure(state="disabled")
            self.gift_box.configure(state="readonly")
      
    def change_click(self, event=None):
        print(int(self.change_txt.get())-1)
        driver.switch_to.window(driver.window_handles[int(self.change_txt.get())-1])

    def tipBtn_click(self, event=None):
        driver.find_element_by_css_selector('.c-button-op.button-icon-m.button-pay.js-tipBtn').click()
        
    def slider_scrollX(self, event=None):
        '''スライダーを移動したとき'''
        print(str(self.scale_var_X.get()))
        
        self.groval_X = self.scale_var_X.get()
                
        '''driver.execute_script("$('body .playerContainer .c-popup.popup-dialog').css('top', '"+str(self.groval_X)+"%')")'''
        
        driver.execute_script('var css="body .playerContainer .c-popup.popup-dialog{top : '+str(self.groval_X)+'%}"; var head = document.getElementsByTagName("head"); var style = document.createElement("style"); style.type = "text/css"; if (style.styleSheet){ style.styleSheet.cssText = css; } else { style.appendChild(document.createTextNode(css)); } head[0].appendChild(style);')
    

    def slider_scrollY(self, event=None):
        '''スライダーを移動したとき'''
        print(str(self.scale_var_Y.get()))
        
        self.groval_Y = self.scale_var_Y.get()
        
        '''driver.execute_script("$('body .playerContainer .c-popup.popup-dialog').css('left', '"+str(self.groval_Y)+"%')")'''
        
        driver.execute_script('var css="body .playerContainer .c-popup.popup-dialog{left : '+str(self.groval_Y)+'%}"; var head = document.getElementsByTagName("head"); var style = document.createElement("style"); style.type = "text/css"; if (style.styleSheet){ style.styleSheet.cssText = css; } else { style.appendChild(document.createTextNode(css)); } head[0].appendChild(style);')
        
    def time_wait(self, wait):
        '''連投間隔を設定したとき''' 
        print(str(wait))
        if str(wait) != "0":
            print("間隔設定")
            print(str(wait))
            driver.implicitly_wait(wait)
            self.popWindow = driver.find_elements_by_css_selector('.c-popup.popup-dialog.js-popupWindow')
            driver.execute_script("var popWindow = arguments[0]; popWindow.parentNode.removeChild(popWindow);", self.popWindow[0])
            
        else:
            if not self.check_v.get():
                print("checkなし")
                self.yesBtn_clickWait()
            
    def yesBtn_clickWait(self, event=None):
            driver.implicitly_wait(0)
            wait = WebDriverWait(driver, 2)
            wait.until_not(expected_conditions.invisibility_of_element_located((By.XPATH, '//*[@id="js-livePlayerContainer"]/div[1]/div/div/div[2]/div/div[2]/a')))
            driver.find_element_by_xpath('//*[@id="js-livePlayerContainer"]/div[1]/div/div/div[2]/div/div[2]/a').click()

    # startボタンclick時のイベント
    def btn_click(self, event=None):
        
        radio_checked = self.v1.get()
        print("ラジオ:"+str(radio_checked))
        
        '''1の場合、テキストボックス'''
        if radio_checked == 1:
            textbox = self.txt.get()
            sp = int(self.sptxt.get())
            #テキストボックスが未入力かどうか
            if textbox != "":
                #テキストボックスが整数または全角数字かどうか
                if textbox.isdecimal():
                    #繰り返し
                    for i in range(sp):
                        if driver.find_elements_by_css_selector('.c-popup.popup-dialog.js-popupWindow'):
                            # 存在する時の処理
                            self.input_int(textbox)
                        else:
                            # 存在しない時の処理
                            #チップアイコン押下
                            if driver.find_elements_by_css_selector('.c-button-op.button-icon-m.button-pay.js-tipBtn'):
                                driver.find_element_by_css_selector('.c-button-op.button-icon-m.button-pay.js-tipBtn').click()
                                self.input_int(textbox)
                                    
                else: messagebox.showinfo("メッセージ", "数値を入力してください（全角OK）")
            else: messagebox.showinfo("メッセージ", "値を入力してください")
        
        elif radio_checked == 2:
            radiobox = self.gift_box.get()
            print("ギフト:"+radiobox)
            sp = int(self.sptxt.get())
            #繰り返し
            for i in range(sp):
                if driver.find_elements_by_css_selector('.c-button-op.button-icon-m.button-gift.js-giftBtn'):
                    driver.find_element_by_css_selector('.c-button-op.button-icon-m.button-gift.js-giftBtn').click()
                    self.gift_input_int(radiobox)

    def input_int(self, keys):
        wait = self.tip_time.get()
        driver.find_element_by_css_selector('.c-input-text.js-tipAmountText').send_keys(keys)
        driver.find_element_by_css_selector('.c-button-dialpg.js-sendTipBtn').click()
        self.time_wait(wait)
        
    def gift_input_int(self, keys):
        wait = self.tip_time.get()
        list_of_li = driver.find_elements_by_css_selector('.c-popup-gift.js-giftPopUp li')
        data = None
        
        for element in list_of_li:
            data = element.get_attribute('data-name')
            print("data:"+data)
            
            if keys == data:
                print("成功")
                element.find_element_by_css_selector(".c-popup-gift_img img").click()
                driver.find_element_by_css_selector('.c-button-dialpg.js-yesBtn').click()
                print(str(wait))
                time.sleep(float(wait))
                        

# 画面をそのまま表示
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.geometry('500x450') # 画面サイズの設定
    root.title('投げ銭クリッカー（FC2ver）') # 画面タイトルの設定
    app = Application(master = root)
    app.mainloop()




        