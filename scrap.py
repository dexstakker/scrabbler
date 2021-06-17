

import twl
#import pyautogui
#import tkinter.ttk
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from functools import partial
from string import ascii_lowercase


global latestDraw
global paneArray
global e1
global draw_s
global draw_m
global global_button_count
global global_min_word_score


global_button_count = 0
paneArray= []
latestMulti={}
global_min_word_score = 15


pieceMultArr = [1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, \
                               1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, \
                               1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, \
                               3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, \
                               1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, \
                               1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, \
                               1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1, \
                               1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, \
                               1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, \
                               3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, \
                               1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, \
                               1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, \
                                1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1]

wordMultArr = [3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3, \
                               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                               1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, \
                               1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, \
                               1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, \
                               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                               3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, \
                               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                               1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, \
                               1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, \
                               1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, \
                               1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                                3, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 3]


score_dict = {
'a': 1,
'b': 2,
'c': 3,
'd': 2,
'e': 1,
'f': 4,
'g': 2,
'h': 4,
'i': 1,
'j': 0,
'k': 5,
'l': 4,
'm': 3,
'n': 1,
'o': 1,
'p': 3,
'q': 10,
'r': 1,
's': 1,
't': 1,
'u': 1,
'v': 4,
'w': 4,
'x': 8,
'y': 4,
'z': 10,
"ch": 5,
"sh": 5,
"st": 3,
"qu": 7,
"th": 5

}

board = ["","","","","","","","","","","","","", \
"","","","","","","","","","","","","", \
"","","","","","","f","","","","","","", \
"","","","","","","i","","","","","","", \
"","","","","","r","e","a","l","t","y","","", \
"","","","","","","r","","","","","","", \
"","","","","","","c","","","","","","", \
"","d","o","o","r","m","e","n","","","","","", \
"","","","","","","r","","","","","","", \
"","","","","","","","","","","","","", \
"","","","","","","","","","","","","", \
"","","","","","","","","","","","","", \
"","","","","","","","","","","","",""]
global_xarr = [0,1,1,1,1,2,7,2,1,1,1,0,0]
global_yarr = [0,0,1,1,6,1,1,7,1,0,0,0,0]









class App(tk.Tk):
    draw_s = ""
    draw_m = []

    global_current_horiz_high_score = 0
    global_current_horiz_high_word = ""
    global_current_horiz_high_code = ""
    global_current_vert_high_score = 0
    global_current_vert_high_word = ""
    global_current_vert_high_code = ""
    global_horiz_resp = ""
    global_vert_resp = "VERT\n"
    global_button_count = 0

    paneArray = []
    button_text = ""
    e1 = Entry(None)
    letters = ""


    for sq in range(169):
        if len(board[sq]) > 0:
            pieceMultArr[sq] = 1
            wordMultArr[sq] = 1

    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()

        # don't assume that self.parent is a root window.
        # instead, call `winfo_toplevel to get the root window
        self.winfo_toplevel().title("Simple Prog")
        self.working_frame = tk.Frame(self)
        self.second_frame()
        self.do_full_lookup(board, self.draw_s, self.draw_m)

    # print_board dumps copy of the current state of the Scrabble board
    def print_board(self, arr):
        i = 0
        while i < 169:
            # Proceed through all 169 board squares
            if (((i+1) % 13) == 0):
                capper = "\n"
            else:
                capper = ""
            txt = "  "
            c = (i % 13)
            r = (i // 13)
            if board[i]:
                global_xarr[r] = global_xarr[r] + 1
                global_yarr[c] = global_yarr[c] + 1
            if (len(arr[i]) == 1):
                txt = arr[i] + " "
            if (len(arr[i]) == 2):
                txt = arr[i]
            print(txt, end=capper)
            i = i + 1
        print("")

    def handle_blanks(self, round, loadFrame, draw_singles, draw_multi, valDict = {}, blank_count = 0):
        blanks = {0, 0}

        if blank_count == 1:
            for c in ascii_lowercase:
                print("Letter Step: " + c)
                draw_sub = draw_singles + c
                self.do_single_round(round,loadFrame,draw_sub, draw_multi, valDict)
        else:
            if blank_count == 2:
                for c in ascii_lowercase:
                    for d in ascii_lowercase:
                        draw_sub = draw_singles + c + d
                        self.do_single_round(round, loadFrame, draw_sub, draw_multi, valDict)

        self.placeButtons(loadFrame)

    def placeButtons(self, loadFrame):
        self.global_btns.sort(reverse=True)
        for i in range(0,15):
            btn = Button(loadFrame, text=self.global_btns[i], command=lambda txt=self.global_btns[i]: self.execute_word_button(txt))
            pane = Frame(loadFrame)
            pane.pack(fill=tk.BOTH, expand=True)

            # button widgets which can also expand and fill
            # in the parent widget entirely
            btn.pack(fill=tk.BOTH, expand=True)
            paneArray.append(btn)

            # button widgets which can also expand and fill
            # in the parent widget entirely

            btn.pack(side='top')


    def do_single_round(self, round, loadFrame, draw_singles, draw_multi, valDict = {}):
        prev = ['', '', '', '', '', '', '', '', '', '', '', '', '']
        curr = ['', '', '', '', '', '', '', '', '', '', '', '', '']
        anon = ['', '', '', '', '', '', '', '', '', '', '', '', '']
        trail = 0
        self.global_btns = []



        totaldraw = draw_singles
        for entry in draw_multi:
            totaldraw +=  entry

        for y in range(12):
            if global_yarr[y] < 1 or global_yarr[y] > 2:
                continue
            elif (y > 0 and global_yarr[y - 1] > 2) or (y < 13 and global_yarr[y + 1] > 2):
                continue
            else:
                startPos = 0
                first_index = -1
                second_index = -1
                first_char = ''
                second_char = ''
                trail = -1
                for x in range(12):
                    curr[x] = self.gbs(x, y)
                    if y < 1:
                        prev[x] = 0
                        anon[x] = self.gbs(x, y + 1)
                    elif y >= 12:
                        prev[x] = self.gbs(x, y - 1)
                        anon[x] = 0
                    else:
                        anon[x] = self.gbs(x, y + 1)
                        prev[x] = self.gbs(x, y - 1)

                    if curr[x] != '':
                        if first_index == -1:
                            first_index = x
                            first_char = self.gbs(x, y)
                        elif second_index == -1:
                            second_index = x
                            if x > -1:
                                second_char = self.gbs(x, y)

            lead_in = 0
            i = first_index - 1
            while i >= 0:
                if anon[i] == '' and prev[i] == '':
                    lead_in += 1
                    i -= 1
                else:
                    break

            i = second_index
            j = first_index + 1
            broken_pair = 0
            while j < second_index:
                if anon[i] != '' or prev[i] != '':
                    broken_pair = 1
                    j = second_index
                    break
                j += 1
            trail_out = -1
            i = j
            while i <= 12:
                if anon[i] == '' and prev[i] == '':
                    trail_out += 1
                    i += 1
                else:
                    break
            print("GAME: Processing Row " + str(y) + ("FIRST half (1 of 2)"))
            self.do_one_row_lookup(y, totaldraw, self.draw_m, first_char, first_index, second_char, second_index, lead_in,trail_out,broken_pair,loadFrame)
            if (second_index != -1):
                print("GAME: Processing Row " + str(y) + ("SECOND half (2 of 2)"))
                self.do_one_row_lookup(y, totaldraw, self.draw_m, second_char, second_index, '', -1, 0, trail_out, broken_pair, loadFrame)

        for x in range(12):
            if xarr[x] < 1 or xarr[x] > 2:
                continue
            elif (x > 0 and xarr[x - 1] > 2) or (x < 13 and xarr[x + 1] > 2):
                continue
            else:
                startPos = 0
                first_index = -1
                first_char = ''
                second_index = -1
                second_char = ''
                y = 0
                trail = -1
                for y in range(12):
                    curr[y] = self.gbs(x, y)
                    if y < 1:
                        prev[y] = 0
                        anon[y] = self.gbs(x + 1, y)
                    elif y >= 12:
                        prev[y] = self.gbs(x - 1, y)
                        anon[y] = 0
                    else:
                        anon[y] = self.gbs(x + 1, y)
                        prev[y] = self.gbs(x - 1, y)

                    if curr[y] != '':
                        if first_index == -1:
                            first_index = y
                            first_char = self.gbs(x, y)
                        elif second_index == -1:
                            second_index = y
                            second_char = self.gbs(x, y)

            lead_in = 0
            i = first_index - 1
            while i >= 0:
                if anon[i] == '' and prev[i] == '':
                    lead_in += 1
                    i -= 1
                else:
                    break

            i = second_index
            j = first_index + 1
            broken_pair = 0
            while j < second_index:
                if anon[i] != '' or prev[i] != '':
                    broken_pair = 1
                    break
                j += 1

            trail_out = -1
            i += 1
            while i <= 12:
                if anon[i] == '' and prev[i] == '':
                    trail_out += 1
                    i += 1
                else:
                    break
            print("GAME: Processing Row " + str(x))
            self.do_one_col_lookup(x, totaldraw,  self.draw_m, first_char, first_index, second_char, second_index, lead_in,trail_out, broken_pair, loadFrame)
            if (second_index != -1):
                self.do_one_col_lookup(x, totaldraw, self.draw_m, second_char, second_index, '', -1, 0, trail_out, broken_pair, loadFrame)

        self.placeButtons(loadFrame)



    def draw_word_route(self, strCommand):
        btntxt = strCommand.split(",")
        if len(btntxt) < 3:
             return

        backupBoard = copy.deepcopy(board)
        self.add_word_to_board(backupBoard, btntxt)
        self.print_board(backupBoard)


    def execute_word_button(self, strCommand):
        print("GAME: Word chosen - " + strCommand)
        if (global_debug_flag == 1):
            self.draw_word_route(strCommand)
        else:
            txt = strCommand.split(",")
            if len(txt) < 3:
                return
            self.add_word_to_board(board, txt)
            self.second_frame()



    def add_word_to_board(self, b, txt):
        print_points = int(txt[0])
        print_word = str(txt[1])
        print_idx = int(txt[3])
        print_pos = str(txt[2])
        print_idx = int(txt[3])
        print_direction = int(txt[4])
        print_length = int(txt[5])
        step_idx = 0
        if (print_direction == 1):
            print_idx += 13
            step_idx += 13
        else:
            step_idx += 1
        idx = print_idx
        for z in range(6,print_length+6):
            b[idx] = txt[z]
            pieceMultArr[idx] = 1
            wordMultArr = 1
            idx += step_idx





    def do_one_row_lookup(self, thisrow, totaldraw, multi, fixed_letter, fixed_index, fixed_letter2, fixed_index2, lead_in, trail_out, broken_pair, loadFrame):
        global global_current_horiz_high_score
        global global_button_count
        print("DO_ONE_ROW_LOOKUP( row " + str(thisrow) + ")")
        totaldraw += fixed_letter + fixed_letter2
        answer = list(twl.anagram(totaldraw))
        newans = []
        second_index_backup = fixed_index2

        for i in answer:
            if 1:
                fixed_index2 = second_index_backup
                translations = {}
                remain = 0
                count = 0
                pts = 0
                idx = 0
                x = i
                y = i
                if fixed_letter in i:
                    pts = score_dict.get(fixed_letter)
                    # First fixed letter is encoded into new word as "0"
                    x = i.replace(fixed_letter, "0", 1)
                    y = i.replace(fixed_letter, "", 1)
                    translations[hex(0)] = fixed_letter
                    idx += 1
                else:
                    continue

                idx += 1
                if fixed_index2 != -1:
                    if (fixed_letter2 == '' or x.find(fixed_letter2) >= 0):
                        continue
                    pts = pts + int(score_dict.get(fixed_letter2))
                    # Second fixed letter is encoded into new word as "1"
                    x = x.replace(fixed_letter2, "1", 1)
                    y = y.replace(fixed_letter2, "", 1)
                    translations[hex(1)] = fixed_letter2

                # Thumb through any multi-letter squares and replace them with digits in codeword
                for idx, j in enumerate(multi):
                    blen = len(i)
                    y = y.replace(j, "", 1)
                    idx += 1
                    indexStr = str(idx)
                    x = x.replace(j, indexStr, 1)
                    translations[str(hex(idx))] = j
                    totaldraw = totaldraw.replace(j, "")
                # Then repeat for individual characters
                for c in totaldraw:
                    idx += 1
                    blen = len(y)
                    x = x.replace(c, str(idx), 1)
                    y = y.replace(c, "", 1)
                    translations[str(hex(idx))] = c

                valid = 1
                for c in x:
                    if c < '0' or c > '9':
                        valid = 0
                        break
                if valid == 0:
                # print("Error: ", i, ": invalid multi-char letter")
                    continue

                # Determine linchpin index (how far into the word is the fixed index)
                linchpin_pos = x.find("0")
                startindex = fixed_index - linchpin_pos  # this is where the word begins
                margin = fixed_index2 - fixed_index  # these are the letters
                if startindex < (fixed_index - lead_in):
                    #print("Error: ", i, ": start index leaves no room")
                    continue
                if startindex + len(x) > 12:
                    # print("Error: ", i, ": end index leaves no room")
                    continue

                #if startindex <= fixed_index2 and startindex + len(x) > fixed_index2:



                if fixed_index2 >= 0 and margin > 0:
                    endpin_pos = x.find("1")
                    if (endpin_pos == -1):
                        fixed_index2 = -1
                        trail_out = margin - 1
                    else:
                        if (endpin_pos - linchpin_pos) != margin:
                            #print("Error: ", i, ": indexes don't line up")
                            continue

                if (fixed_index2 == -1):
                    trail_out = (13 - fixed_index)


                if len(y) > 0:
                    continue

                remain = (len(x) - startindex) + 1
                endpos = startindex + remain
                if fixed_index2 > 0:
                    if (startindex + len(x)) <= (fixed_index2 - 1):
                        continue


                remain = len(x) - (linchpin_pos + 1)
                if (linchpin_pos > lead_in or remain > trail_out):
                    #print("word " + i + " rejected")
                    continue

                vert = 0
                pts = self.check_score(thisrow, x, translations, startindex, fixed_index, fixed_index2, lead_in, trail_out, vert, i)

                newans.append(i)


                button_text = i + ",[" +  str(startindex+1) + ":" + str(thisrow+1) + "]," + str((thisrow * 13) + startindex) + ",0," + str(len(x))
                for ch in x:
                    k = int(ch)
                    ltr = translations[str(hex(k))]
                    button_text += "," + ltr
                pfx = "0"
                if pts < 10:
                    pfx = "00"
                button_text = pfx + str(pts) + "," + button_text
                self.global_btns.append(button_text)
                continue



    def do_one_col_lookup(self, thiscol, totaldraw, multi, fixed_letter, fixed_index, fixed_letter2, fixed_index2, lead_in, trail_out, broken_pair, loadFrame):
        print("do_one_col_lookup row = " + str(thiscol))
        totaldraw += fixed_letter + fixed_letter2
        answer = list(twl.anagram(totaldraw))
        newans = []
        second_index_backup = fixed_index2

        for i in answer:
            if 1:
                fixed_index2 = second_index_backup
                translations = {}
                things_changed = 0
                remain = 0
                count = 0
                pts = 0
                idx = 0
                x = i
                y = i
                if fixed_letter in i:
                    pts = score_dict.get(fixed_letter)
                    # First fixed letter is encoded into new word as "0"
                    x = i.replace(fixed_letter, "0", 1)
                    y = i.replace(fixed_letter, "", 1)
                    translations[hex(0)] = fixed_letter
                    idx += 1
                else:
                    continue

                idx += 1
                if fixed_index2 != -1:
                    if (fixed_letter2 == '' or x.find(fixed_letter2) >= 0):
                        continue

                    pts = score_dict.get(fixed_letter2)
                    # Second fixed letter is encoded into new word as "1"
                    x = x.replace(fixed_letter2, "1", 1)
                    y = y.replace(fixed_letter2, "", 1)
                    translations[hex(1)] = fixed_letter2

                # Thumb through any multi-letter squares and replace them with digits in codeword
                for idx, j in enumerate(multi):
                    cf = x.find(j)
                    if (cf != -1):
                        blen = len(i)
                        y = y.replace(j, "", 1)
                        idx += 1
                        indexStr = str(idx)
                        x = x.replace(j, indexStr, 1)
                        translations[str(hex(idx))] = j
                    totaldraw = totaldraw.replace(j, "")


                # Then repeat for individual characters
                idx += 1
                for c in totaldraw:
                    blen = len(y)
                    x = x.replace(c, str(idx), 1)
                    y = y.replace(c, "", 1)
                    if len(y) < blen:
                        translations[str(hex(idx))] = c
                        idx += 1

                # Determine linchpin index (how far into the word is the fixed index)
                linchpin_pos = x.find("0")
                startindex = fixed_index - linchpin_pos  # this is where the word begins
                margin = 0
                if (fixed_index2 > 0):
                    margin=fixed_index2 - fixed_index  # these are the letters
                if startindex < (fixed_index - lead_in):
                    #print("Error: ", i, ": start index leaves no room")
                    continue
                if startindex + len(x) > 12:
                    # print("Error: ", i, ": end index leaves no room")
                    continue
                if fixed_index2 >= 0 and margin > 0:
                    endpin_pos = x.find("1")
                    if (endpin_pos == -1):
                        fixed_index2 = -1
                        trail_out = margin - 1
                    else:
                        if (endpin_pos - linchpin_pos) != margin:
                            #print("Error: ", i, ": indexes don't line up")
                            continue

                if len(y) > 0:
                    continue

                remain = (len(x) - startindex) + 1
                endpos = startindex + remain
                if fixed_index2 > 0:
                    if (startindex + len(x)) <= (fixed_index2 - 1):
                        continue

                remain = len(x) - (linchpin_pos + 1)
                if (linchpin_pos > lead_in or (trail_out > 0 and remain > trail_out)):
                    #print("word " + i + " rejected")
                    continue

                vert = 1
                pts =  self.check_score(thiscol, x, translations, startindex, fixed_index, fixed_index2, lead_in, trail_out, vert, i)

                newans.append(i)

                button_text = i + ",["  + str(thiscol+1) + ":" + str((startindex+1))  + "]," + str(((startindex-1) * 13) + thiscol) + ",1," + str(len(x))
                for ch in x:
                    k = int(ch)
                    ltr = translations[str(hex(k))]
                    button_text += "," + ltr
                pfx = "0"
                if pts < 10:
                    pfx = "00"
                button_text = pfx + str(pts) + "," + button_text
                self.global_btns.append(button_text)
                self.global_vert_resp += str(i) + " in col " + str(thiscol) + " for " + str(pts) + " points\n"
                continue




    def gbi(self,x, y):
        #Return global coordinate index of game board square for x,y
        return (x + (y * 13))

    def gbs(self,x, y):
       #Return contents of gameboard square for x,y
        return board[self.gbi(x,y)]

    ############################################################
    # ROW Lookups
    ############################################################
    def do_full_lookup(self, board, draw_singles, draw_mult):


        root = tk.Tk()

        subframe = Frame(root)
        subframe.pack()
        frame = Frame(subframe)
        frame.pack()
        pane = Frame(frame)










    def GetPieceMultiplier(self,x,y):
        return pieceMultArr[gbi(x,y)]

    def GetWordMultiplier(self, x, y):
        return wordMultArr[gbi(x,y)]

    def GetPieceMultiplierByIndex(self, idx):
        return pieceMultArr[idx]

    def GetWordMultiplierByIndex(self,idx):
        return wordMultArr[idx]

    def show_word(encodedWord, transationArr):
        actualWord = ""
        # Iterate over index
        for element in range(0, len(encodedWord)):
            actualWord += translationArr[int(element)]

        print("Actual Word: " + actualWord)
        return actualWord


        # lead_in and trail_out
    def check_score(self,thisrow, testword, dic, start_index, fixed_index, fixed_index2, lead_in, trail_out, vert, inp):
        letters_score = 0
        letters_mult = 1

        step = 1
        if vert == 1:
            step = 13
            word_start_index = (start_index * 13) + thisrow
            word_end_index = word_start_index + (13 * len(testword))
        else:
            word_start_index = (thisrow * 13) + start_index
            word_end_index = word_start_index + (1 * len(testword))
            step = 1
        idx = word_start_index
        src_index = 0
        word_mult = 1
        while src_index < len(testword):
            #print("src = " + str(int(testword[src_index])))
            charcode = dic[hex(int(testword[src_index]))]
            letter_score = int(score_dict[charcode]) * self.GetPieceMultiplierByIndex(idx)
            letters_score += letter_score
            word_mult *= self.GetWordMultiplierByIndex(idx)
            src_index += 1
            idx += step
        score = letters_score * word_mult
        return score






    def __init__(self,parent=None):
        super().__init__()
        self.working_frame = tk.Frame(self)
        self.second_frame()
        self.do_full_lookup(board, self.draw_s, self.draw_m)


    def first_frame(self):
        self.working_frame.destroy()
        self.working_frame = tk.Frame(self)
        self.working_frame.pack()

        maxItems = Spinbox(self.working_frame, from_=5, to=30)
        maxItems.delete(0, "end")
        maxItems.insert(0, "15")
        maxItems.pack()
        tk.Button(self.working_frame, text='Reload', command=lambda: self.redux(maxItems.get())).pack()
        drawbtn = tk.Button(self.working_frame, text="See", command=lambda: self.toggleMap())
        drawbtn.pack()

        # do_single_round does a full round of lookups, both directions
        if (self.blank_count > 0):
            self.handle_blanks(round, self.working_frame, self.draw_s, self.draw_m, {}, self.blank_count)
        else:
            self.do_single_round(1, self.working_frame, self.draw_s, self.draw_m, )

        #tk.Label(self.working_frame, text='Border Frame').pack()
        #tk.Button(self.working_frame, text='Next Round', command=self.second_frame).pack()


    def redux(self, maxItems):
        global global_min_word_score
        global_min_word_score = int(maxItems)
        self.first_frame()

    def toggleMap(self):
        global global_debug_flag
        if global_debug_flag == 0:
            global_debug_flag = 1
        else:
            global_debug_flag = 0


    def second_frame(self):
        self.print_board(board)
        self.working_frame.destroy()
        self.working_frame = tk.Frame(self)
        self.working_frame.pack()
        tk.Label(self.working_frame, text='Single Letter Tiles:').pack()
        e1 = tk.Entry(self.working_frame)
        e1.pack()
        tk.Button(self.working_frame, text='Replenish', command=lambda: self.process_round(e1.get())).pack()



    def process_round(self, inStr):
        print("GAME: New Letters = " + inStr)
        self.blank_count = 0
        valDict = {}
        draw_m =[]
        draw_s =""
        tiles = inStr.split(",")

        for s in tiles:
            if s == "BLANK":
                self.blank_count += 1
            pieces = s.split('=')
            ltrs = pieces[0]
            if len(pieces) == 2:
                val = int(pieces[1])
                valDict[ltrs] = val

            if len(pieces[0]) > 1:
                draw_m.append(pieces[0])
            else:
                draw_s += pieces[0]

        self.draw_s = draw_s
        self.draw_m = draw_m
        self.valDict = valDict
        self.first_frame()



if __name__ == '__main__':
    App().mainloop()
