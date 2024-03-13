import os
import shutil
import time

from PIL import Image

import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
from tkinter import filedialog

import mung2
import nox2
import kaes4go as en4py
import multiprocessing as mp

class mainclass:

    def __init__(self):
        self.tool = en4py.toolbox() # kaes4 tool
        self.pw = '' # password
        self.kf = en4py.getkf('기본키파일') # keyfile
        self.hint = '' # hint
        self.current = '' # current storage name
        self.bytes = '' # current encrypted bytes
        self.status = 'idle' # idle pre open

    def pack(self, paths): # paths str list를 받아 바탕화면에 png로 패킹
        try:
            shutil.rmtree('temp471')
        except:
            pass
        os.mkdir('temp471')
        temp = xenon.data0
        with open('temp471/png128.png', 'wb') as f:
            f.write(temp)
        img = Image.open('temp471/png128.png')
        img = img.resize( (2048, 2048) )
        img.save('temp471/png2048.png')
        mtool = mung2.toolbox()
        mtool.pack(paths, 'temp471/pack.dat', False)
        ntool = nox2.toolbox()
        ntool.set(16, 'temp471/png2048.png')
        res = ntool.pack('temp471/pack.dat', False, 'png')
        out = os.path.join(os.path.expanduser('~'),'Desktop')
        for i in range( 0, res[0] ):
            shutil.copy(f'temp270/{res[1]}{i}.png', f'{out}\\{res[1]}{i}.png')
        shutil.rmtree('temp471')
        shutil.rmtree('temp270')
        return f' 바탕화면으로 이동되었습니다. \n 일련번호 : {res[1]}, 전체개수 : {res[0]} '

    def unpack(self, path): # png folder path str 받아 언팩하고 현재폴더에 풀기
        try:
            shutil.rmtree('temp471')
        except:
            pass
        os.mkdir('temp471')
        temp = xenon.data0
        with open('temp471/png128.png', 'wb') as f:
            f.write(temp)
        img = Image.open('temp471/png128.png')
        img = img.resize( (2048, 2048) )
        img.save('temp471/png2048.png')
        mtool = mung2.toolbox()
        ntool = nox2.toolbox()
        ntool.set(16, 'temp471/png2048.png')
        res = ntool.detect(path)
        if res[0] == 0:
            raise Exception('novalidPIC')
        else:
            ntool.unpack( [ path, res[0], res[1], res[2] ] )
            res = mtool.unpack('temp270\\result.dat')
            if res == -1:
                raise Exception('novalidFILE')
            elif res == 1:
                raise Exception('notvalidCRC')
        count = 0
        for i in os.listdir('temp261'):
            count = count + 1
            os.rename(f'temp261/{i}', i)
        shutil.rmtree('temp471')
        shutil.rmtree('temp270')
        shutil.rmtree('temp261')
        return f' {count}개의 파일이 \n 정상적으로 언패킹되었습니다. '

    def mainfunc(self):
        win = tkinter.Tk()
        win.title('KOS PW Manager 4')
        win.geometry("600x450+100+50")
        win.resizable(False, False)

        def mf0(): # new
            time.sleep(0.1)
            if self.status == 'idle':
                a = time.strftime( '%Y-%m-%d_%H:%M:%S', time.localtime( time.time() ) ) # 시간 문자열
                b = 'KOS PW Manager 4\n사용을 환영합니다.' # 내용
                temp = bytes(f'{a}\n{b}', 'utf-8')
                temp = self.tool.enwhole(b'0000', self.kf, b'initial password\n0000\nwith basic keyfile', temp) # encryption bytes
                with open('new0.png', 'wb') as f:
                    f.write(temp)
                tkinter.messagebox.showinfo('New Storage', ' 새 KPWM4 저장소가 생성되었습니다. \n 현재 프로그램과 같은 폴더 상에 \n new0.png 파일입니다. \n 파일 이름을 목적에 맞게 바꾸십시오. ')

        def mf1(): # view
            time.sleep(0.1)
            if self.status == 'idle' or self.status == 'pre':
                temp = filedialog.askopenfile(title='파일 선택', filetypes=( ('png files', '*.png'), ('all files', '*.*') ), initialdir="./").name # 저장소 파일
                self.current = temp
                try:
                    hint = str(self.tool.view(temp), 'utf-8')
                    with open(temp, 'rb') as f:
                        self.bytes = f.read()
                    nonlocal status
                    status.set('pre')
                    self.status = 'pre'
                except:
                    hint = '올바른 KAES4\n파일이 아닙니다.'
                nonlocal win
                nonlocal hstr
                self.hint = hint
                hstr.set(hint)
                win.update()

        def mf2(): # save
            time.sleep(0.1)
            if self.status == 'open':
                a = time.strftime( '%Y-%m-%d_%H:%M:%S', time.localtime( time.time() ) ) # 시간 문자열
                nonlocal view2
                view2.set(f'Last Save {a}')
                nonlocal tbox1
                b = tbox1.get('1.0', tkinter.END)[0:-1]
                content = bytes(f'{a}\n{b}', 'utf-8')
                self.bytes = self.tool.enwhole(bytes(self.pw, 'utf-8'), self.kf, bytes(self.hint, 'utf-8'), content) # encryption bytes
                with open(self.current, 'wb') as f:
                    f.write(self.bytes)

        def mf3(): # save close
            mf2()
            if self.status == 'open':
                nonlocal tbox1
                nonlocal view2
                nonlocal view3
                nonlocal in4
                nonlocal hstr
                nonlocal in6
                tbox1.delete('1.0', tkinter.END)
                view2.set('Last Save -')
                view3.set('PW -')
                in4.delete(0, tkinter.END)
                hstr.set('-')
                in6.delete('1.0', tkinter.END)
                self.pw = ''
                self.hint = ''
                self.current = ''
                self.bytes = ''
                nonlocal win
                nonlocal status
                status.set('idle')
                self.status = 'idle'
                win.update()

        def mf4(): # save exit
            mf2()
            if self.status == 'open':
                self.pw = ''
                self.hint = ''
                self.current = ''
                self.bytes = ''
                nonlocal win
                win.destroy()

        def mf5(): # import
            time.sleep(0.1)
            if self.status == 'idle':
                temp = filedialog.askdirectory( title='폴더 선택', initialdir=os.path.join(os.path.expanduser('~'),'Desktop') )
                try:
                    b = self.unpack(temp)
                    tkinter.messagebox.showinfo('변환 완료', b)
                except Exception as e:
                    b = f' 오류 메시지 \n {e} '
                    tkinter.messagebox.showinfo('변환 실패', b)

        def mf6(): # export
            time.sleep(0.1)
            if self.status == 'idle':
                temp = filedialog.askopenfiles(title='파일들 선택', filetypes=( ('png files', '*.png'), ('all files', '*.*') ), initialdir="./")
                names = [ ]
                for i in temp:
                    names.append( i.name.replace('/', '\\') )
                try:
                    b = self.pack(names)
                    tkinter.messagebox.showinfo('변환 완료', b)
                except Exception as e:
                    b = f' 오류 메시지 \n {e} '
                    tkinter.messagebox.showinfo('변환 실패', b)

        def mf7(): # pw reset
            time.sleep(0.1)
            if self.status == 'open':
                nonlocal in4
                nonlocal view3
                self.pw = in4.get()
                if len(self.pw) < 3:
                    view3.set( 'PW ' + '●' * len(self.pw) )
                else:
                    view3.set( 'PW ' + self.pw[0] + '●' * (len(self.pw) - 2) + self.pw[-1] )
                nonlocal hstr
                nonlocal in6
                self.hint = in6.get('1.0', tkinter.END)[0:-1]
                hstr.set(self.hint)
                mf2()
                nonlocal win
                win.update()

        def mf8(): # status
            time.sleep(0.1)
            if self.status == 'open':
                nonlocal kfpath
                a = '현재 저장소 상태 보기'
                b = f' 저장소 경로 : {self.current} \n 저장소 크기 : {len(self.bytes)} \n 비밀번호 : {self.pw} \n 키 파일 경로 : {kfpath.get()} \n 키 파일 크기 : {len(self.kf)} '
                tkinter.messagebox.showinfo(a, b)

        def mf9(): # read
            time.sleep(0.1)
            nonlocal win
            nonlocal in4
            nonlocal status
            temp = in4.get() # pw 후보
            if self.status == 'pre':
                try:
                    content = str(self.tool.dewhole(bytes(temp, 'utf-8'), self.kf, self.bytes), 'utf-8')
                    self.pw = temp
                    nonlocal status
                    status.set('open')
                    self.status = 'open'
                    a = content[0:content.find('\n')]
                    b = content[content.find('\n') + 1:]
                    nonlocal view2
                    view2.set(f'Last Save {a}')
                    nonlocal view3
                    if len(temp) < 3:
                        view3.set( 'PW ' + '●' * len(temp) )
                    else:
                        view3.set( 'PW ' + temp[0] + '●' * (len(temp) - 2) + temp[-1] )
                    nonlocal tbox1
                    tbox1.insert('1.0', b)
                    nonlocal in6
                    in6.insert('1.0', self.hint)
                except Exception as e:
                    tkinter.messagebox.showinfo('Invalid PWKF', f' 비밀번호 또는 키 파일이 올바르지 않습니다. \n {e} ')

        mbar = tkinter.Menu(win) # 메뉴 바
        menu0 = tkinter.Menu(mbar, tearoff=0) # file
        menu0.add_command(label="New", font = ("맑은 고딕", 12), command=mf0) # 새 저장소 만들기
        menu0.add_command(label="Open (View)", font = ("맑은 고딕", 12), command=mf1) # 기존 저장소 열기
        mbar.add_cascade(label="  File  ", menu=menu0)
        menu1 = tkinter.Menu(mbar, tearoff=0) # save
        menu1.add_command(label="Save", font = ("맑은 고딕", 12), command=mf2) # 저장
        menu1.add_command(label="Save & Close", font = ("맑은 고딕", 12), command=mf3) # 저장 후 창 초기화
        menu1.add_command(label="Save & Exit", font = ("맑은 고딕", 12), command=mf4) # 저장 후 종료
        mbar.add_cascade(label="  Save  ", menu=menu1)
        menu2 = tkinter.Menu(mbar, tearoff=0) # io
        menu2.add_command(label="Import", font = ("맑은 고딕", 12), command=mf5) # 사진에서 저장소로
        menu2.add_command(label="Export", font = ("맑은 고딕", 12), command=mf6) # 저장소에서 사진으로
        mbar.add_cascade(label="  Io  ", menu=menu2)
        menu3 = tkinter.Menu(mbar, tearoff=0) # action
        menu3.add_command(label="PW reset", font = ("맑은 고딕", 12), command=mf7) # 비밀번호 재설정
        menu3.add_command(label="Status", font = ("맑은 고딕", 12), command=mf8) # 저장소 상태 보기
        menu3.add_command(label="Open (Read)", font = ("맑은 고딕", 12), command=mf9) # 저장소 읽기
        mbar.add_cascade(label="  Action  ", menu=menu3)
        win.config(menu=mbar)

        status = tkinter.StringVar()
        status.set('idle')
        in0 = tkinter.Entry(win, font = ("Consolas",17), width=45, textvariable = status, state = 'readonly')
        in0.place(x=5, y=10)

        frame = tkinter.Frame(win) # 왼쪽 프레임
        frame.place(x=5,y=55)
        tbox1 = tkinter.Text( frame, width=25, height=15, font = ("맑은 고딕", 14) ) # 내용 텍스트박스
        tbox1.pack(side="left", fill="y")
        scrollbar1 = tkinter.Scrollbar(frame, orient="vertical")
        scrollbar1.config(command=tbox1.yview)
        scrollbar1.pack(side="right", fill="y")
        tbox1.config(yscrollcommand=scrollbar1.set)

        view2 = tkinter.StringVar() # 마지막 저장 시간
        view2.set('Last Save -')
        label2 = tkinter.Label( win, font = ("맑은 고딕", 14), textvariable = view2 )
        label2.place(x=300, y=50)
        view3 = tkinter.StringVar() # 비밀번호 표시
        view3.set('PW -')
        label3 = tkinter.Label( win, font = ("맑은 고딕", 14), textvariable = view3 )
        label3.place(x=300, y=90)

        in4 = tkinter.Entry( width=27, font = ("맑은 고딕", 14), show = '●' )
        in4.grid(column = 0 , row = 0)
        in4.place(x=300,y=130) # pw 입력창

        def func5():
            time.sleep(0.1)
            try:
                temp = filedialog.askopenfile(title='파일 선택').name
                kfpath.set(temp)
                self.kf = en4py.getkf(temp) # 키 파일 바이트 업데이트
            except:
                kfpath.set('기본키파일')
                self.kf = en4py.getkf('기본키파일')
            nonlocal win
            win.update()
        kfpath = tkinter.StringVar() # 키 파일 경로
        kfpath.set('기본키파일')
        but5 = tkinter.Button(win, text = '. . .', font = ("맑은 고딕", 14), command = func5)
        but5.place(x = 300,y = 170)
        label5 = tkinter.Label( win, font = ("맑은 고딕", 14), textvariable = kfpath )
        label5.place(x=350,y=175) #키 파일 경로 표시

        hstr = tkinter.StringVar() # 힌트 표시
        hstr.set('-')
        label6 = tkinter.Label( win, font = ("맑은 고딕",14), textvariable = hstr )
        label6.place(x=300,y=220) #힌트 표시 라벨
        in6 = tkinter.Text( width=27, height=4, font = ("맑은 고딕",14) )
        in6.grid(column = 0 , row = 0)
        in6.place(x=300,y=330) #힌트 입력창

        win.mainloop()

class xenon:
    data0 = b""
    data0 = data0 + b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00\x80\x08\x02\x00\x00\x00L\\\xf6\x9c\x00\x00\x18bIDATx\x9c\xed]\xe9n#\xc7\xb5>U\xd5{\xb3)R\xbb,)\x13\xdb\xb8\xb6\x11\xe3\x02\x89\x81,o\x90\xa7\xbb\xefq\xdf$\xbf\x12'
    data0 = data0 + b'\xc4p`#\x9e\xc4\x1a[\xb3H\x94Hq\xed\xa5\xd6\xfb\xe3\x13\x0b\x8c-M\xec\x9b\xa1\xd44t0\x18p4\xadf\xf7\xf9\xea\xacu\xea\x1c\xf6\xbf\x9f\xff\x0f\xad\x93x\xc0\xb4\xd6A\x10\x10Q\xd34A\x10\x84a\xa8\x94\xe2\x9ck\xad\x9b\xa6\xd9\xde\xde\x9eN\xa7\xbd^\xaf'
    data0 = data0 + b'\xaek\xfc\xfc\xce\xfb\x08!\x94R\x8c1k\xad1&\xcb\xb2(\x8a\xca\xb2\xb4\x96pC\xadu\x1c\xc7\x8c\xdd~\x9d\xd6:MS\xa5\x94R*\x8a"\xc6\x98R\x8a\x88\x8c1\xf8\n\xb6B\xce9\xa5T\x1c\xc7\xc6\x18k->4M\xc3\x18\x0bE\xb0V\xfe\xac\xf7\xeeDd'
    data0 = data0 + b'\x8c1\xc68\xe7\x88\x08\xbc#"\xad5cL\x08\x11\xc7\xb1\xb5v6\x9bYk\x85\x10Q\x14\xe1\x82\xfb\xee\x13\x04A\x14EM\xd3,\x16\x8b\xa6i\x9csQ\x94\x08!p\x7f\xb0\x921\x86\xef\x92R\x82\xa1RJ\xfc$\x08\x824M\x81\xa2\xd6\xda9\xc79w\xcei\xad'
    data0 = data0 + b'\xc30\xc4g\xe7\x9c\xb5\x96\x88\x82 \x10B8c\xd7\xca\x9f\xb5\x03\x10\x86\xa1\x10\xc2\x7f\x06\xa7\xc20L\x92DJi\xade\x8cmmmeYf\x8c\x91R\x82}w<h\x10\xe0\xef8\x8e\x85\x10eY:\xe7\x92$\xd1\xda*\xa5\xc0w\xb0\x1bL\x8c\xe3\x98\x888\xe7'
    data0 = data0 + b'a\x18\x12\x911&\x0c\xc3 \x08\xea\xba\xc6\xf3`\x11\x04A\xc0\x18\x83Lh\xad\xf1\xebZk"\xba\xefI\xde-\xad\x1d\x00\xbc0\x18\xcd9\x87\xae\x08\xc3\xb0,\xcb\xa6i\x84\x10X\xd7X\x92UU\x15Eq\xe7}\x9a\xa6!"\xa5\x14\xf4\x18\xe7\x1c2A\xc4\xa4\x94B'
    data0 = data0 + b'\x880\x0c\xa1^\x80\x84\xd6ZJ\t\x8d\x07`\xac\xb5\xb8\x89\x10\x82s\x1e\x04\x01\xa0\xa2%\xaf\xa1\x00\xc30\x84\x04p\xce\xf1a\xadt\xb7\xc2}\x87\x14\x04\x01^\x95\x88\xe28\x86\xa4\xc7q\x0c\xd5\xbc\xbd\xbd\x1d\x04\x81Rj:\x9d\n!z\xbd\x9e\xbd\x87\x82 \xe8t:'
    data0 = data0 + b'a\x18j\xad9\xe7I\x92DQ$\x84\xc0\xcd\xa1\x9a\xa0\xd0\xe38\x8e\xe38\x8a"p\x1f\n*\x0c\xc38\x8e\x9ds\xb8I\x18\x86i\x9aB\xd7CSA\xc2\xa2(J\xd3\x14\x02\x01\x9c\xd6\xce\x9f\xb5\x7fA\x10H)G\xa3Q\x10\x04Y\x96\xe1\x9d\xa3(\x8a\xa2h8\x1c'
    data0 = data0 + b'^^^*\xa5`Q\x85\x10\xb3\xd9\x0c\x8c\xf8!\xd5u\r\x96\x01\x8f\xf9|\xae\x94\xea\xf7\xfbD\x0e\xe2\xa5\x94\xba\xba\xba2\xc6\xec\xee\xee\xc6q\x0cH8\xe7\x8b\xc5b<\x1e\xf7z\xbd~\xbf\xdf4M\xd34777\xc6\x98^\xaf\x97e\x19\x11\x01?o\x9f\xa4\x94\x83'
    data0 = data0 + b'\xc1@)\xb5\xb3\xb3\x13\x86\xe1\xba\xd5\xd0\xda\x01(\xcb\xf2\xe2\xe2\xe2\xeb\xaf\xbf\xc6\xf2/\x8a\xa2\xaa*"\x12B|\xf9\xe5\x97\xd7\xd7\xd7i\x9a\xfe\xf6\xb7\xbf\xedv\xbb\x93\xc9\xe4\xaf\x7f\xfd\xebh4\xba\xf3>EQ|\xf0\xc1\x07;;;B\x88\xab\xab\xab\xaf\xbe\xfa\x8a\x88'
    data0 = data0 + b'>\xfb\xec\xb3n\xb7Kd\x19s\xf3\xf9\xec\x1f\xff\xf8ZJI\xf4\xf1\xe1\xe1aU-\x00\xd5\x8b\x17/^\xbcx\xf1\xec\xd9\xb3O>\xf9Dk]\xd7\xf5\xf3\xe7\x7f\x9f\xcdf\x1f~\xf8\xe1\xfb\xef\xbf/\x04\xb3\x96\x82\x80k\xad\xac\xd5\xce\x99\xf1x\xfc\xf7\xbf\x7f%\xa5\xfc'
    data0 = data0 + b'\xf8\xe3\x8f\x8f\x8e\x8e\xd6\xad$\xd6\x0e@\x9a\xa6Z\xeb\xeb\xeb\xeb,\xcb\x18cy\x9e[k\xa3(\x1a\x0c\x06\xa3\xd1h>\x9f\xc7q\x9c\xe7y\x96e\xf3\xf9\xbc\xaa*x,?\xa4\x17/^\x14E\xb1\xb3\xb3S\x14\xc5p8|\xf9\xf2%4\x0cVz\x1c\xc7777\x83'
    data0 = data0 + b'\xc1`\xb1X\x1c\x1f\x1f3\xc6\xb0\xfc\xa5\x94\x8b\xc5b0\x18loo\xe3\x8b\x8c1\xd3\xe9\xf4\xe2\xe2bgg\x07\x9a\xcd9g\x8c\x816\x13BTU\xf5\xfa\xf5\xeb\xa6iNOO\xc30\xd4\xf2n\xaf\xec]\xd1\xda\x01\x80\xb5\x84\x97\x92$\xc9x<\x86\xbc\x9f\x9f\x9f\x0f'
    data0 = data0 + b"\x06\x83^\xaf\xf7\xbb\xdf\xfd\x8e1V\x96%\x94O]\xd7\x1f|\xf0\xc1\xaf\x7f\xfd\xeb\xc5b\x01e\x15\x04\xc1\x17_|\xa1\x94\x1a\x0e\x870\x1ey\x9e\xf7\xfb\xfd\xd9l6\x9f\xcf\xb7\xb7\xb7'\x93I\x92$^\xb0\xc6\xe31X\xcf\x18\x93R\x8e\xc7\xe3,\xcb\xf6\xf7\xf7\x95R"
    data0 = data0 + b'\xc6\x18\xf8\xa0B\x88\xc1`\x80k\xe28\x86a\x97Rv:\x9d\xc1`\x007!I\x12\xa5\x14\xdbt\t\x00\xeb\xb1\xd0`x9\xe7\xb3\xd9\xec\xfa\xfa:\x8e\xe3\xdd\xdd\xdd$I\xe0\xfc\xe1\xfa8\x8e\xb3,+\x8a\x02\xde\x0b\x1c\x1e(k\xd8X"\xc2j%")\xa5sN'
    data0 = data0 + b"\x08\x01\x1b\x00?\x12^)-\xdd\x18\xf8\x94\xde\xcd\x87\x8f$\x84\x90R\x96e\xd9\xe9t\xe0\x8f\xc2s\xc5\x0f\xf1E\xd6Z\xce\xb9[\xaf\x00\xac\xdf\x0b\xc2;{\xd7\x1b\xa1\xc0\x9b7o\x06\x83AQ\x14'''Y\x96!&\x02s!.p+\xbd\xd7\xe4\xefCD\x80\x13"
    data0 = data0 + b'n\xfeb\xb1p\xce\x86a\xc0\x18\x95\xe5BkE\xe4\xea\xba2F\x139!\xb81\xbaij\xceY\x1cGBp\xe7,\xe7Lk\x15Ea]W\xe3\xf1M\x14\x85\xd6\x1a\xce\x99s6M\x93\xb2\\\x8c\xc77\x8c\x11cd\x8c~\x00/h\xed_@DX\x8f`k\x10'
    data0 = data0 + b'\x04UU}\xf7\xddwHB\xec\xee\xeeBGq\xce\xb1B\x9b\xa6\x91Rb9k\xad\xe1\xd1\xfb\xc8\x08K\x15N$\x11\xf9\x10\x9a\x88\xe6\xf39\xfe\x0b\x11\x06.\x96RB\xbd$I\x02\x81\xc0\xd2\x86\xc2\x19\x0e\x87Dt\xbb\xd2\x9d\x8b\xa2h:\x9dN&\x13\x88\x94\xb5\xf6'
    data0 = data0 + b'\x01B\xb1\x87\x90\x00"\xc2\x1a\x8f\xa2\xc8Z;\x1a\x8d.//\xb7\xb6\xb6vwwa\xa2\xbd\x1a\xc1\xea\xc6g\xfc:~\x02\xb9\x01\xf7\xc1\xe5,\xcb\x84\x10\xb0\x13H+\xc1\x85\xcd\xf3\xbc\xae\xeb\xaa\xaapq]\xd7Z\xeb$I\x92$\xf1\xeb\xc0\xdf|<\x1e#\x9f\x81\xf0'
    data0 = data0 + b'\xcdZ{ssSU\xd5}\xae\xf0:\xe8!\x00\x00\x83\xe0nO&\x937o\xde(\xa5NOO\xb7\xb7\xb7\x91;[\xd5\xb9P\xfa\xab\x00p\xce}\xb6\x07\xde\xba\x10"MSx,PY\xf0v\xd24\xed\xf5zJ\xa9\xb2,\x11c\xd7u\xed\x9c\xcb\xb2\x0c\x16\xc5/'
    data0 = data0 + b'\x7f\xadu\x14E\xf3\xf9|<\x1e\x03\x12\xceyUU\xf8\'\xdc\x84e$\xbc\xde`\xf8!\x00\xc0\xfa\x85W~yyyqq\x91e\xd9\xf1\xf1qQ\x14X\xd1A\x10 "E\xd2\xc2\x1bd\xfc\xfa2\xe5@\xb4\x02@\x92$\xc8\x8f\x1ac\x8cU\x8d\xac\xaaz\x91fq'
    data0 = data0 + b'\xaf\xdf5V\x95\xd5\x9c\x0b\xd2F\xd6M\xc9\xb8\xcb\xf2D\x04\xccX\xc5\xb8\xb3N\x87\x91P\xbaI\xd2H\xaa\xfaf<d\xdc1\xee\xb8\xa0\xf9b:_L\x83\x90\x07!\xb7NsA?\x87T\x04\xf8\x8b\x0fZ\xeb\xd1h4\x99L:\x9d\xce\xd6\xd6\x16\x0c)L4t='
    data0 = data0 + b't1-\x17\xbe7\xbf\x1e\x80\xd5T\xa5wp\xad\xb5ZY\xadu\x1c\xa5Y\x969\xcb\x94R\x9c\x05\xc6\x18%\r\xe7<\n\x13\xc6\x98\xd1\xceK\x00rs\xc6\x98\xc5bq\xcb\x08\xce\xeb\xba\xae\xeb\x1aw\xf6\x86a\xdd\xfcY;\x00Q\x14\x8d\xc7c\xc6\xd8\xfe\xfe\xfe\xf3\xe7'
    data0 = data0 + b'\xcf\x9f?\x7f\x1eE\xd1\xa7\x9f~\x8a\x98\x08\xaf\r}\x9d\xa6i\xd34\xf0\xe8\x9b\xa6\xf1\xfe\x0fL7\x14\x08\xb4\xbfR\xaa\xd7\xebq\xce\x9b\xa6)\xcb\xaa[\xf4\xae\xae\xae\x03\x11eY\x9e&y\x92\xa4\xb3\xe9\xc29"\xc7G\xa3\x1br\xbc(\xbaF;\xc68#\xe1,s'
    data0 = data0 + b'\x961\x12;\xdb{i\x92\xff\xf3\x1fgi\x927\xb5\xe2,\x18^\xdf\x94\x8b\xfa\xf4\xe4Y\x1c\xa5\x8c\x845\xe4\xf3\xb8\xeb\xa3\x07\x92\x00\xc6\xd8t:\x1d\x8f\xc7q\x1c\x1f\x1c\x1ct\xbb]\x9f\x89\x04y\xa5/\xa5D6\r\xe9L\\&\xa5D\x00\x01\xbf\x08v%\x8a""'
    data0 = data0 + b'*\xcb\x12\tQ\xe7(\xcb\xb2,\xcb\x85\x10M\x03?\n[\x08a\x1c\xc7\x9c\x0b\xc6\x98s\xb7\xc1\x81\x10\x02\xe1w\xd34\xd3\xe9\x14\xc24\x9f\xcf\x19c\x88\xd8W\x9em\xbd,z\x08\x00\x90V\x9cN\xa7WWWA\x10\x1c\x1c\x1c\xf4\xfb\xfd\xd5kV3\xef\xc8Q\xc3\x0c'
    data0 = data0 + b'\xfa|\xfd\x0fS\xf6\xb0\xc3\xce\xb9\xd9lFDUUYk\xbb\xdd.\x92\x9d\x8b\xc5\x02\xbe,B?Xl\xa8\x14\xa8;!D\xb7\xdb\xdd\xda\xdaj\x9a\xe6\xfa\xfa\x1a^\xe9\xf5\xf552\xb2\x08\xd6V}\x81\xf5\xd1C\xc4\x01>\x10\x83\x8f\x0f\x13\xfa\xbd\\\xbc\x8fr\xb1\x00'
    data0 = data0 + b'\xe1>\x82Y\xc6\x98$I\xea\xba\x86\x19\x07\x1f9\xe7y\x9e\x13\x11<\xce\xc5b\xe1\x9c\xcb\xf3\x1c\x1egY\x96~K\x00\x99"\xc0IDB\x08\xb8dp\x99\x8c1\xc3\xe1P\x08\x01\x8f(\xcb2,\x0e\xef\xf5\xae\x9b9\x0f\x91\x0b\xc2k\xc0\x17\x1c\x8f\xc7\xc3\xe1\x10\x0bv'
    data0 = data0 + b"\xd5\xd7\xf4\xaf*\xa5<??\xc7\x96,v\xcd\x84\x10\xc3\xe1\x10K\x12\x112<W\xe4'\xa4\x94Zk\xa4\x92`6:\x9d\xce\xd5\xd5\x15\x1c$\xa5\xd4\xd6\xd6V\x14EJ)\x1fj ?\x81\x9d\xb88\x8e\xa7\xd3\xa91\xe6\xe6\xe6\x06\xf9m\x18\xa7\x87\xd9\x0e\xa3\x07\xcb\x05"
    data0 = data0 + b'\x19c\xba\xdd\xee\xfe\xfe>\xb2\xd3\xaf_\xbf\xde\xdb\xdb[]\xfb\xfe\x85\xb5\xd6\x93\xc9D)5\x9f\xcf\x93$Y,\x16Y\x969\xe7\xf6\xf6\xf6z\xbd\x9ew~\xb0?\x83X\xb7,\xcb\xaa\xaa\x10\x9ai\xad\xe1\xdd"0F\x14\x16\xc7qUU\xab*\x05\xf2\xd1\xedv\xbb\xdd'
    data0 = data0 + b'\xee|>\x9fL&\xc3\xe10\x0c\xc3\xbd\xbd=D\t\x10Y\xe7\x1c\xd1z\x91X;\x00x\x19)%\xe7\xfc\xf4\xf4t<\x1e\x9f\x9f\x9f\x9f\x9f\x9f\xef\xee\xee\xde)\xe0EQ\xec\xed\xed\xed\xef\xef\xcf\xe7\xf34M\xcb\xb2\x84R\x8a\xa2\xa8\xdb\xedb\xf9\x1bc\x90[f\x8cU'
    data0 = data0 + b'U5\x99L\xa4\x94\xfb\xfb\xfb\x1e\x00\xce\xf9\xcd\xcd\r6\x7f\xd24\x05\x90\xb4\x145\xbf\x11_\x14E\xaf\xd7{\xf9\xf2\xe5\xe5\xe5\xe5\xcd\xcdM\x9e\xe7x*\xa5\x14\xb2\x87\xd6ZF\xebu\x84\x1e\xa2*\x02\x11\x93\xd6\xba\xdf\xef\xef\xec\xec\x9c\x9d\x9d]__\xfb\x0bV\x97?'
    data0 = data0 + b'\x11\xcd\xe7\xf3\x8f>\xfa\xe8\x93O>Ar\x18\xfe\xa8\xdf\xacG\xd6\x13\xf7D\x18\x81\n\t\x14\xaa \x8eCq\xca|>\'"\xec=\xc0_\xc2\x1d|\xe2\x01{\xfaY\x96a\xc3\xae,\xcb<\xcf\x8b\xa2\xf0\xb1\xde\x03\x18\x00z\x00#\x8c\xe4\x8c\x8f\xfe\xf7\xf7\xf7\x9f={'
    data0 = data0 + b'6\x1a\x8d\xfe\xf2\x97\xbf \xf1\x00x\x88h<\x1ec\xb7\x16\xd7;\xe7\x90i@\xf1\x04\x11\xd5u-\xa5\xf4U\x0e\xc8Z;\xe7\x06\x83\x01D\x04\xbb=\x88\x15\x16\x8b\xc5\xd5\xd5\x15\xb4\xcal6\x83\xf7\t\x82\x07\x85\xb4\xf3\xc9\xc9I\x10\x04/_\xbeTJ\x1d\x1d\x1d\xd5u'
    data0 = data0 + b'\x9d\xe79D\xf6a2Bk\x07\x00\x89L\x00\x00\x93\x88\x0c\xe8h4\xba\xba\xba\x12B\xd4u\r\xee\xf4\xfb\xfd\xb7\x87\xfe?4\xda>\x9a\x05\x000\xecI\x92@h`xa{}P\x8d\xef\xf2\x96)\x8e\xe3n\xb7\xeb#\x03<\xa7\xb7\xd5?\x077\x14o\x8bZ\x8f\xa6'
    data0 = data0 + b'i\xba\xdd\xee\xc9\xc9I\x9e\xe7\xa3\xd1\xe8\xe5\xcb\x97\xf02\xc1\x8bN\xa7\x03Q\xb8\x93V\xb3\x98\x1e\x00$S\xa7\xd3i\x18\x86y\x9e\x03l\xec\xdd\xd7u\xdd4\x8d\xd7?\x1e\x00\xb8\xb6D\x84\x0fI\x92\xec\xec\xec@:{\xbd^\x14E0W\x08\xfa~\x0e\xfb\x01>\xdf\t'
    data0 = data0 + b'U\xc39\xdf\xdd\xdd=>>Fbn8\x1c\xa6i\n\xcd\x00\xaf\xf1\xbe\xfbx\xe3I+\x15;\x9dN\x87\x88\x16\x8bE\x92$\xd8\xdb\xa2ei\tb\x0e\xb8@D\xb4\x9a\xe2F,\r\xe9Ai\x8c\xd6:\xcf\xf3\xad\xad-H\x00\x1e\xfba\x9c\xd1\x87\xa8\x0b\xc2\x0bGQ'
    data0 = data0 + b'\x04\xb5\x1eE\xd1\xfb\xef\xbf_\x14\xc5d29;;C\x94\x84\xe4\xfe[r/\x00\x80V\xd4\x08\x11\xc1\xe1\x81=\xf0@"D\x80\xa3\x99\xe79\xca\x1d}=\xa8\xcf\xebA\xc53\xc6\x10<\xf7z\xbd$I\x1e&\xf8Z\xa5\x87\x90\x00\xafO\x83 h\x9aFk\xed\x85\xe0'
    data0 = data0 + b"\xfc\xfc\x1c\xbbZ\xc0\t\xab\xf5-\xb7\x02w\xbc\x8b\x02\x83)\x84@\x94\x07\x11\xb1\xd6v:\x1dp\x1c?\xc7\xa2\xc6\x1d\x006`\xc0?;\x9d\xce\xee\xee\xee\xce\xce\x0e\x11\xf9\x8c\xec\xcf'\x1b\xaa\x94\xf2~\x0b\x12j(r\xfe\xf0\xc3\x0f\xf3<\x9f\xcf\xe7ggg(\x1dD"
    data0 = data0 + b'\xfe\xe7\xbe\xfbx\t\xa0%\xe3\x88\x08\xc1\xb0\xaf\xc1\x82\x00!\xe8\x03\x1e~\xdb\xc0\xef\xba@\xf9\xf8mNkm\x9e\xe7\xbf\xf8\xc5/\xfa\xfd>rG>\x02\x80S\xbbn\xfe<\x1c\x00x7(\x04)\xe5{\xef\xbdW\x14\x05c\xec\xfc\xfc\x1c\xa5\x0c\xc8\x88\xfd\x98{z\xd5'
    data0 = data0 + b'\x0cf\xf9\x9d\x03(z\xe4y\x90}\x03\x0c\xbe<\x9b1F\x84\xed\x07\xd4\xc1!\x1aH\x0f\x0e\x0e\xf2\xbc\x83Mh!\x84s\xc0[<\x806Z;\x00\x9d\xac\x98M\xe6dY\x1ag\x17\xaf/C\x11%Qj\x945\xca\xfe\xd7\x87\x1f\xa5q6\x1eM^|\xf3m\x9ev'
    data0 = data0 + b'&7\xd3$J\xadv\x01\x0f\x17\xb32O;\xccqg\xc8jG\x96q\x12F\xd9PDV;\xab]("\xdc3\x0e\x93\x80\x87Y\x92s\x12\xaa\xd1\x01\x0fC\x119Cu\xd9\xa4q\x96D\xa9jt\xaf\xdb7\xcaZ\xed\xb44d\x99\xd5\x96\x93\xa8\xcb:\x89\xd2,\xc9'
    data0 = data0 + b'f\x93y\x96d\xb2Vq\x18\xf7\xb7\xb6/\xdf\\\xc6a\x12\x87\xf1\xe4f\x9a\xa7\x9du\xf3g\xed\xb1\x86\x94\xf2\xf8\xf8\xb8\xdb\xed\xfa\r[\x18I\xe7\xdc\xe1\xe1!\xd2\x90\xfd~\xdf9\xd7\xedv\x7f\xf5\xab_\x1d\x1c\x1c\x1c\x1c\x1cxk\x01\x15\xff\xbd\xcd\x83U\xfa\xec\xb3\xcf'
    data0 = data0 + b'&\x93\tb\x8b\xba\xaeiY\xfb\xfe\x87?\xfc\x81\x88vvv|\xf0\x8c2\xe1(\x8a>\xfd\xf4\xbf\x91\xba@Y.j,\x9a\xa6\xd1\xda\x1a\xd3\xf4z\xdb(\x0b\xebt:?R"\xff\x13b\xeb>!\xe3#&h\x18\x84]i\x9ab\xe3\x85\x88\xea\xba\xf6\x15p\xd8}'
    data0 = data0 + b'\x841@)9\xf2\n\xf0\xcd\xef\xbc\x7f\xa7\xd3A\xc5\\\x92$\xd8\x1b\xc8\xf3\\)\x85\xfc\x0fR\xa4UU\xc1\xd3\x87\x05\xc2w\xe1|\x0eL\x02\x14#\xf0K\xd3\x14\xd9Sl\x07\xad;\x14x\x88\x03\x1ax\x19\x1f\xfe\xc0\x17D\xcd\x08\xd2\xcbp\x81n\x8f\x04-w\xf0\xc5'
    data0 = data0 + b'\x92\x10B\xdf\xe7 \xf94\x11\xb6\xde\x00!\xa2\nx\xa5\x08\xbeh\x99Gb\xcb\xf2/\x18aX\xda\xc5b\x11\x86!\x1c6c\x0cR \xb4\xe2n\xad\x8f\x1e"\x0e@,\x86\x97G\xe5>\x18m\x97\x87\x87p\r\xf4\x0c\xeasWku\xe0\x11\xdew\xff\xc5b\xe1\xe38'
    data0 = data0 + b'\xfc\n\xd2\xa5\xd8X\xc6\x0e\x1a-\x81\xf7%Y\x10D$-\x10$"\x99\x81\xb0\x19i\x0c"\x82\xfb\xb0^\xfe\xac\xfb\x0b\x9a\xa6\x81\xce\xa1ea\x04-\x83\x03\xbfC\x02\xa7\x10\x077 \x07\xb4r\xa0\x0c?\xbf\xcf#\x04\xcbh\x99t\xa2e\xbe\x01\x92\x84\x05\x0e[\x02?'
    data0 = data0 + b'\xd5\xcb\x04V\xc0\xaaJ\xc4W`\x95\xd0\xf2\x94\xd9\xba\xf9\xf3\x10n\xe8\xear\xf6\xa5\x86>\x14\xf2e?~\x85\xfa\xf5\xee\x8bP\xde"\x01\xf05}\xac\x07\xf0\x90g\x85\xae\'"\xa8#Z\t\xc4\x10\x8b\x81\xe9\xbe\xf4\x08\xe4#\x06\xac\x8cu\xf3g\xed\x12\x80\x83A\xbe\x8c'
    data0 = data0 + b"\x199K\x04\x07\xd0K\xe0`\x14E\xb0\x8a\xd0\xe3\x9e\x05P/oa\x04\n\xe2\xfc\xba\xf6\x98a\x0f\xd9kv_X\xe7\xcb~\xbc?FD^\xe1 h\xc0\x7fa\xefz\xdd\x18\xac\xdd\x0bz\xa2\xb7\xd3CTE<\xd1[\xe8\t\x80G\xa6'\x00\x1e\x99\x9e\x00xdz"
    data0 = data0 + b"\x02\xe0\x91\xe9\t\x80G\xa6'\x00\x1e\x99\x1e\xee0\xd4\x9a\xc8\xfd\xc4ms\xf6\xa0;\xbe\xff\x9e\x9e$\xe0\x91\xe9\t\x80G\xa6'\x00\x1e\x99\x9e\x00xdz\x02\xe0\x91\xe9\t\x80G\xa6'\x00\x1e\x996\x06\x00\x94/\xd0\xf2\xc4\x87\xdf>\xc39\x0bl\xef\xf4z\xbd\xb7\xd4O"
    data0 = data0 + b'\xb4\x936)\x10\xf3\x95\nD\xe4O[0\xc6\xbe\xfc\xf2Klr\x9d\x9d\x9d\xa1\x05\x8e?\xf4\xd1~\xda\x18\x00|\x99;\xe4\xc0\xef\xd1_]]\xfd\xe9O\x7fB;\xc0\xc1`\xf0\xfb\xdf\xff\x1e}\xe56E\x0e6\xe3)iy\x9e\xc2\xd7\xa6\xa3\xd6\x9a\x88\x86\xc3a\xd34'
    data0 = data0 + b'\xd8\xc8\x15B\x9c\x9c\x9c\xe0\xa0\xfdc?\xef\x8f\xa5\x8d\x01\xc0\x1f-Bi\x05J\xde\xa4\x94\xaf^\xbd*\x8a\x02\xd5>GGGGGG\xbe\x14w#hc\x00@q\x03`\xf0\xa7\x18\x87\xc3\xe1`0\x00\xf7\xcb\xb2\xc4Y\x97\xaa\xaaPd\xb8\x11\xb416\x00j\xc7\x17'
    data0 = data0 + b"\x9e\x08!\xca\xb2|\xf5\xea\x15ZI3\xc6\x8a\xa2x\xf6\xec\x99\xb5\x16GM7E\x086F\x02VJKQ)m\x9b\xa6\xba\xba\xbat\xceL\xa7c\xade\xaf\xd7-\x8a\x02'RQ\xd8\xbb\x11\xd4:\x00\x1c\xfb\xe1\x1f\xeb\x98M\xf3\xa4j\xca0\x0ef\x8bY\xd6I\x1d"
    data0 = data0 + b's\xd7\xa3\xeb\xd9b\x86n\x87D\xae\xd3\xc9ww\xb7\x9d3\xce\x99$\x89\x88\xd6\xdem\xec\x9dP\xeb\x00\xb8\x8f\x96=S\xaa4M\x95\x92Z\xeb\xe1\xe8\n\x8d\xc5\x18w8mZ\xd7U\x9a&\xbe\xbat#hc\x00@\x85:Zx[k\xe7\xf3\xf9\xe5\xe5\xa5\xf7J\xfb'
    data0 = data0 + b"\xfd\xfe\xc1\xc1A]\xd7hl\xf3\x04\xc0\xbb'DaD\x84X\xec\xea\xeaj>\x9f\xe3\xd0\x9d1\xe6\xe0\xe0\x00\xa31\x1e\xac\xcf\xcf\xbb\xa2\x8d\x01\x00\xa5\xed\xfe$\xfb\x9b7o|\xf5y\x18\x86\xfb\xfb\xfb8f\xd34\xcd[j\xd9[H\x1b\x03\x80\xefd\xa8\xb5^,\x16"
    data0 = data0 + b'h/\x86\x94\xdc\xee\xeenQ\x148a\x80Q>O\x00\xbc{\xf2\xcd\x0e\x82 \xb8\xb8\xb8\xc0\x0c\x19\xa8\x9a_\xfe\xf2\x97l9\x1f\xc5\xb7@~\xec\xe7\xfd\xb1\xb41\x00\xe0\xcc\x05z\xc0]]]\xe1\x88\x07\xa2\xb3\xc3\xc3C\x1cvD3\x9b\xb7\x1c\xa9l!mL$L'
    data0 = data0 + b"D\xb0\x01777\x17\x17\x17B\x08!\xb8\xb5\xf6\xe4\xe4\x04[\x028\x19)\xa54\xc6\xb2\x95yV\xab\xc7l8\xe7\xd42l6\x06\x00\xf4.I\xd3\xf4\xec\xec\xcc\x9f72\xc6\xec\xed\xedeY\x86I@\xec\xb6\xeb'\xe7\x9c\xa3c\x16\xa8\xcd~\xd1&\x01\x80#D/"
    data0 = data0 + b"^\xbc\x80K\x8a\x9f\x1c\x1d\x1dEQ\xd4\xd4\xcd\xc5\xc5\xc5R\x05\x11c\xec\xe0\xe0\x80\x88\x18\xa3\xefIC\xdb\x02\x84\x8d\x01\x00>\xcfx<\x9eN\xa7\xd0EuS\x1e\x1d\x1d!\xf5\xd64\xcd\xeb\xd7\xaf\xdf\xbcy\xc3\x183\xc6\n!\xfe\xf8\xc7?\x12\x11\x02\xb2'\tx\x07"
    data0 = data0 + b'\x84\x03\xdf\xdf~\xfb-_\x0e|`\x8c\x1d\x1f\x1f\xd3r0\x87\xb5v2\x99\x04A\xe0\x1c!Z\xf6\xe7\xb3\x1f\xfb\xd9\xdfF\x1b\xe3\x05\x11Q\xd34\x18\x9e\x84\xdd\xb1\xad\xad\xad\xfd\xfd}"\xf2\xdd\x07\xfc\x11\xd4;}\xa1v"\xb11\x00(\xa5\xaa\xaa\x9aN\xa7u]#'
    data0 = data0 + b'\xe2=>>\xce\xf3\x9cs\x8e3\xb0\xbe\x1f\xae]\xce\xf1\xf1-j\xfc\xf9\xe1\x16R\xfb\x01@L\xeb\xa4\x94R6\xe8R\x1c\x86a\xd34\xfb{\x87\x8c\x84\xe0\xa1\xd1\xce,G\xff$I\x12E\xa1\x10\xfc_\x7f\xbd\xbd\xd4:\x00\x04\x0f\x03\x11-{-\n\xc6Hk%\x02'
    data0 = data0 + b'\x96\xe7\xd9\xdf\xfe\xf67\xa5TQ\x14eYmmm\x1f\x1c\xbcg-\xab\xeb\x06=\x8c\xb5\xd6a$\xac\xd3J7\x8c;"\xc79\xf3G\xbd\x19\t\x0c\x0fx\xec\xf7\xfb>\xb5\x0e\x00\xf0\x8b\x88\x9c\xbb\x9dM\xcb\x05\x11\xd1\xf5p U\r\xdb\xcby\xb0\xbf\xbf\xcfY \x84'
    data0 = data0 + b' \xe2w\xb7wf\x96\x18\x96\xbf%\x87\xd7\\\xfd\xbb-\xd4\xae\xa7\xa1\x7f\x01\xc0\xf9~\x97\xce\xb9\xf3\xf3s\xb4\xb7AA\xca\xb3g\xcf\xe8\xad=$6\x85\xda\xf8\x02n9\xf3\x01\xe9O!D\xd34\x98\xbb\n\x95\x12E\xd1\xe1\xe1ak]\xfb\x9fD\xad\x03\xc0\xcfg\x80'
    data0 = data0 + b'\x17\x8f\xbf\xa7\xd3)\xbaa\x81\xe9EQ\xa03\xe8\xe3>\xea;\xa1\xd6\x01\xe03\x07\xbe\xd5\xaa\x94\x12\xe9O\xbf\xfdrpp\x005\xb5Ay\xff\xfb\xa8\x8d\x00x\xb6\xc2\x97\xaf\xeb\x1a\xdb\xbf\xa8\x85\xce\xb2\xec\xe4\xe4d\xe3\xaa\xa0\xef\xa3\xd6\xbd\x83[\x8e|\xa3%\x00R\xca'
    data0 = data0 + b"\xc9dBK\xed\x94$\xc9\xee\xee\xee\xc3t\xd6~\x00j\xdd;h\xad1\xd5])e\xadM\x92\xe4\xec\xec\x0c\xdd\xfc\xa7\xd3i\x1c\xc7\x1f}\xf4QY\x96\xe8\xfe\x0fS\x81\x1e\xf8\xf8'J\xb2\xf0\xbb\xc8\x9e\xfa&\xc4\xbec_\xab\xa8u\xc9\xb8\xdb\xe6c\x9c\xa1\xdf\xf7x"
    data0 = data0 + b"<^\x9d>\xd2\xef\xf7\xbb\xddn\x92$\xddnW\x08\xa1\xa5\xb4\xd6\x06\xc1\xedp\x9f0\x0ca'\xd0\x17\xd09\xe7\x96c\xf7\xd0\x10\x91s\xb2-3\xdd\xad\x03\xe0\xb6q\xbf\x10\xe8@\xfc\xcd7\xff\x9cL&\xbe\xa1\xe4\xce\xce\x0e\xf2\x10\xd8\x81\xc1\xa2\xe6\xfc\xb6\xdb3ZX"
    data0 = data0 + b'"|\xbb\xcd\x0e)c\x8c\xe1L\x11\x91\x94\x9a\xc8\xc6\xcb&\x7f-\xa16\x02\xe0\x93h\x9c\xf3\x8b\x8b\x0b4\xf5\xc4\x88\x86\xc3\xc3\xc3(\x8a\xe6\xf3*\xcb2\xc6n\x1b\xd2\x85a@\xe4\xa0\x8b`\x18\x92$A\xfd\xba\xe0\x0c\xfb\xf8\xb8\xb7\x10\xacm\x12\xd0:\x1b\xe0\x87Ma'
    data0 = data0 + b'\xa2\x00&\x881\xc6f\xb3Y\x1c\xc7H\xfb\xa8%\x11\x11:\xff5M\xb3\xda%\x94\x880\n\x0er\x80\x8b}\x07\xd7VQ\xeb$\xc0\xae\xcc\xca{\xf5\xea\xd5|>Gr\x9f\x88\xd0p=\x8e\xe3\xad\xad-\xce\xb9\xd1\x8eq\x17\x86!cNk\xe5\x91\x83^B\x07bk'
    data0 = data0 + b'\x98o\tk\x8ca\xeciK\xf2\xdf\x11j{\xac5A\x10\xbcz\xf5JJ\x99w\xd2\xa6i\xb6\xb6\xb6NOO\x97\xa3y"\xa5\x149n\xac\n\xc3\x90\xf3\xdb\xbe\xc5\x98\xc2\xe3C\x04\xa5\x94\x92\xd6\x18\x93\xa5\x98\xcec\x19s\xbae\x87\xf7Z\x07\x80\xb1\x8a\x8b\xd0\x1aM'
    data0 = data0 + b'\x14\x8cFCx\x93UU\x8dF\xa3\x9b\x9b\x9b\x17g\xdfUU\xd5\xe9\x14J\xa9(J\x94RD6\x0c\x03\xce\xf9w\xe7/\xa6\xd3i\xa7\xd3\x81\xca\xfa\xf3\x9f\xff\x1c\x04\x81\xd1.\xcb\xf2\xe3\xe3\xd3\xde\xd6\xf6m\x8a;h\x97\xd6m\x1b\x00V\x08f\xadJ\x92\xf8\xec\xec\x9b'
    data0 = data0 + b'\xe9lL\xb7\xf9|\x1b\x86\xe1\xe7\x9f\x7f\x8e\x8b.//\xfd/h\xad\xb1\x19\x19\xc5A\x96eU\xb5H\x92D\x08~v\xf6\xcfN\xa7;\x1a\x8d\xe2(\xed\xf7\xfbGGGM\xad\xac\xb5D\xedJ\xe1\xb5\r\x00"r\x18<n\xac\x82\t\x85z\xb9\xcf~r\x1eq\xce\x8d'
    data0 = data0 + b'U\xcb1\x1a1\xe7\xe4\x9c\x11B\x10Y\xdf\xa1\x1a\x17[k\xb9h\x97\x15h\x1d\x00\xb7\x83\x1e\x95\xd5\xca2\x12\xe4\xb8\xd1\xceY\xe6\xee\tb9\xbfM\xde)\xa5\x18C\xf7bC+\xd3\xe7!\x1f\xf0\x88\x1e\xf6U~\x14\xb5\x0e\x00\xc68\xdc\x96N\xa7\x83Cw~\x98\xf0'
    data0 = data0 + b'\x9d\xd7\xa7ij\x8c\xb1N___/\x163?k\xf5\xf4\xf44MS%]\x10\x04i\x9a\xa3\x8a\x94s\xfe\xa4\x82\xfe=\x81S\x98_\x8b\xecB]\xd7EQ\xdcy\xf1m/v\xab\xbe\xf8\xe2\x8bo\xbf\xad\x18c\xd6R\x18\xc6\xbf\xf9\xcdo\xd24\xb5\x86K)\xc30'
    data0 = data0 + b'\xf1\xb7%\xd7\xae@\xacm\x00pc4\xaan1r\xd3O\x01\xab\xaa\xea\xce_@e\x1cr\x15J\x990\x14\xb0\x19Q\x14\x85a\x1c$Q\x14\xc5Rj\xadP\xa7\xe5\x88x\xabJ%\xda\x06\xc0m3\x14k\xad1\xdaZW\xd7\r\xa6($Ir\xe7\xf5\x93\xc9\xd49'
    data0 = data0 + b'\x8b\x91\xcdR\xca$\xe9:\xd78\xe7\xe6\xf3\xb2\xaee\x9a\xe4\x8cq\xadM "T-\xf2\x96%D[\x07\x00\x12\x06~\x0e\x03\x11a@\xcf}\x12\x80\xf9;a\x18\x05"\xc2\xf8\xf8\xb2\x9c+\xa5:\x9d\x8e5\x14\x04a\x10\x04\x9ca\x939PJ\xf1\x96%#Z\x07\x00'
    data0 = data0 + b'&9\xd0JV\x8e\x88\xder\xf0\xd19\xe6\xfbx \xed#D(D\xa8\x95E\x0eCJ\xe9,&\xec\xb9\x16\x1a\xe1v\x85\x85\xff_\xc2[\xb0e\xfd\xcf\x9d\xff{O\xf9\xd0cS\xeb$\xe0?]\x13wc\xd0^\xda\xb0\xc7\xbd\x9f\xee|\x11\xd6\xcej\xb8Uj\xef\x93'
    data0 = data0 + b'\xfdX\xfa\xe1\x92w\x9c\xdc}\n\xa7uZh\xf3\x01 Z)\xfd\xbc\x8b\xbf\xee\xed\x16\xe2\x91\xa9\x8d\xcf\xf4\x9fQ\xeb\xd6\xf8\xdb\xe9\xe7\x07\x00\x11\xb1%\x0c\xabo\xe7\x88\xb5.\x17M-\x04\x80\xb9\x9f\xf6\xa7\xa9\xcb,\x8dU#91\xe6x]6Y\x92ki\x04\x0b\xc8'
    data0 = data0 + b':\xb2Np\n\x03\xce\x99cd8s\xad\xcaCP\x0b\x01\xf8\xa9\x84(\x0c\xe7\xf40\xfb\x16\x87\xe8\xff5p\xb3+\x7f\xdaE-\x8c\x03~\x1a\x01\x80 \x08\x8e\x8e\x8e\x92$\xc1g_\xd8K\xcb\x82\xea\xd6\xd2\xc6\x03\x80B.\x00ppp\xe0S\xa1eY\xfak\xda\x8c'
    data0 = data0 + b'\xc1\xc6\xab ?\r\x17\xd5\x89~f\xab?\x19\xe9\xb9\xdfN\x186^\x02\xfc\xf0a\x9cgBm\x16\xa6\xb5\xfak\xda\xc9z\xd0\xc6\x03\xe0\x96c\xdf\xb1\xe41\xdf\xd9\x17c\xf9kZX\x17\r\xdax\x15\xe4\xa7E\xc3\x17\x02\xd3}u\xa9\xff\xdcZ!\xd8x\t\x00\xad\x9e'
    data0 = data0 + b"\x85\xdf\x88\x0e\x05\x9e6^\x026\x9d\x9e\x00xdz\x02\xe0\x91\xe9\t\x80G\xa6'\x00\x1e\x99\x9e\x00xdz\x02\xe0\x91\xe9\xff\x00\x1a\xbd\xdc\x89\x8eOh\x0e\x00\x00\x00\x00IEND\xaeB`\x82"

if __name__ == '__main__':
    mp.freeze_support()

    k = mainclass()
    k.mainfunc()
    time.sleep(0.5)