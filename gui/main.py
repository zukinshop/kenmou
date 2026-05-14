import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import Qt, QUrl

kenmo_ten_commandments=[
    "一、余計に使うな",
    "二、簡単には買うな",
    "三、捨てるな",
    "四、無駄使いするな",
    "五、贈り物はするな",
    "六、組み合わせだけは買うな",
    "七、きっかけを感じたら逃げろ",
    "八、季節を感じろ",
    "九、流行は無視しろ",
    "十、混乱は高みの見物だ"
]

#winsow_title="嫌儲技術部員"
window_title="ケンモハック - 機能テスト"
class KenmoNativeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(window_title)
        
        self.resize(400, 300)

        # 縦並びのレイアウト
        layout = QVBoxLayout()
        
        # ヒーローラベル
        hero = QLabel("(ヽ´ん`)")
        hero.setStyleSheet("font-size: 80px; color: black;")
        layout.addWidget(hero)

        # デフォルトブラウザを開く嫌儲リンク
        kenmou_link_label = QLabel('<a href="https://greta.5ch.io/poverty/">嫌儲で教養をつける</a>')
        kenmou_link_label.setOpenExternalLinks(True)  # これをTrueにするだけ
        layout.addWidget(kenmou_link_label)

        # Pythonの関数を実行するボタン
        # btn = QPushButton("Pythonスクリプトを実行")
        # btn.clicked.connect(self.run_python_script)  # クリック時に関数を呼び出す
        # layout.addWidget(btn)

        # テキスト
        text = "嫌儲10訓\n\n"
        for i in kenmo_ten_commandments:
            text=text+i+"\n\n"
        #text = text + "テスト行\n" * 30 #（スクロール確認用）
        long_label = QLabel(text)
        layout.addWidget(long_label)

        self.setLayout(layout)

    # 実行させたいPythonの処理
    #def run_python_script(self):
        #print("Pythonの処理が実行されました！")
        # ここにスクレイピング処理やファイル操作などを書くらしい

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # スクロール機能の追加 QScrollAreaとやらがスクロール機能を許すらしい。
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)  # 中身に合わせてリサイズ
    
    # メイン画面をスクロールエリアの中に入れる
    main_widget = KenmoNativeApp()
    scroll.setWidget(main_widget)
    scroll.setWindowTitle(window_title)
    scroll.resize(400, 300)
    scroll.show()
    
    sys.exit(app.exec())