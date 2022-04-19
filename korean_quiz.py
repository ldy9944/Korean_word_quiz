from random import *
from quiz4 import *

data = {
        '얼죽아' : ('凍死してもアイスアメリカノー', '早速やっつけよう', 1),
        '단짠' : ('甘い塩辛い', '堅苦しいケチ', 1),
        '갈비' : ('食べ物の名前', '見るほどうざい', 2),
        '슬세권' : ('チャミスルを飲んでも歩いて帰れる範囲', 'スリッパで動ける範囲', 2),
        '머선129' : ('どういうこと？', '大統領選挙', 1),
        '완내스' : ('マジ私のタイプ', '完全なるスリラー', 1),
        '오저치고' : ('今夜は何食べる？', '今夜チキン食べる？', 2),
        '일취월장' : ('日就月場', '日曜日に酔っ払うと月曜日がヤバい', 2),
        '애빼시' : ('愛嬌抜けると死体', '愛はつまらない', 1),
        '자만추' : ('自然な出会いを追求', '自然から出会う人', 1)
}

already_keys = list()
correct_keys = list()

while len(already_keys) < 10:

        word_key = choice(list(data.keys()))
        ex1 = data.get(word_key)[0]
        ex2 = data.get(word_key)[1]
        answer = data.get(word_key)[2]

        if word_key in already_keys:
                continue

        qustion = word(word_key, ex1, ex2, answer)

        qustion.show_question()
        qustion.check_answer(int(input('=> ')), correct_keys)
        already_keys.append(word_key)
        print()

print(f'あなたの点数は\n{len(correct_keys)}/10点です！')
input('終了するにはEnterを入力してください。')