# #135 「ViewChild ディレクティブ参照」

## 概要
Angular v20におけるViewChildを使ったカスタムディレクティブへの参照取得。ディレクティブのインスタンスにアクセスし、内部状態の操作やメソッドの呼び出しを実現する方法を学ぶ。

## 学習目標
- ディレクティブの参照取得方法を理解する
- ディレクティブのメソッド呼び出しを学ぶ
- ディレクティブの状態管理を把握する

## 技術ポイント
- @ViewChild(DirectiveClass) での参照取得
- ディレクティブメソッドの呼び出し
- ディレクティブプロパティへのアクセス
- ディレクティブの状態操作

## 📺 画面表示用コード

### カスタムディレクティブ
```typescript
@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  private _isHighlighted = false;
  
  constructor(private el: ElementRef, private renderer: Renderer2) {}
  
  toggleHighlight() {
    this._isHighlighted = !this._isHighlighted;
    if (this._isHighlighted) {
      this.renderer.addClass(this.el.nativeElement, 'highlight');
    } else {
      this.renderer.removeClass(this.el.nativeElement, 'highlight');
    }
  }
  
  setHighlight(highlight: boolean) {
    this._isHighlighted = highlight;
    if (highlight) {
      this.renderer.addClass(this.el.nativeElement, 'highlight');
    } else {
      this.renderer.removeClass(this.el.nativeElement, 'highlight');
    }
  }
  
  isHighlighted(): boolean {
    return this._isHighlighted;
  }
  
  setColor(color: string) {
    this.renderer.setStyle(this.el.nativeElement, 'color', color);
  }
}
```

### ViewChildでのディレクティブ参照
```typescript
@Component({
  selector: 'app-directive-ref',
  template: `
    <div appHighlight #highlightRef>
      この要素はハイライトディレクティブが適用されています
    </div>
    <div class="controls">
      <button (click)="toggleHighlight()">ハイライト切り替え</button>
      <button (click)="setHighlight(true)">ハイライトON</button>
      <button (click)="setHighlight(false)">ハイライトOFF</button>
      <button (click)="changeColor('red')">赤色</button>
      <button (click)="changeColor('blue')">青色</button>
    </div>
    <p>ハイライト状態: {{ isHighlighted }}</p>
  `,
  styles: [`
    .highlight {
      background-color: yellow;
      font-weight: bold;
    }
  `]
})
export class DirectiveRefComponent implements AfterViewInit {
  @ViewChild(HighlightDirective) highlightDirective!: HighlightDirective;
  isHighlighted = false;
  
  ngAfterViewInit() {
    console.log('ハイライトディレクティブが準備完了');
    this.updateHighlightStatus();
  }
  
  toggleHighlight() {
    this.highlightDirective.toggleHighlight();
    this.updateHighlightStatus();
  }
  
  setHighlight(highlight: boolean) {
    this.highlightDirective.setHighlight(highlight);
    this.updateHighlightStatus();
  }
  
  changeColor(color: string) {
    this.highlightDirective.setColor(color);
  }
  
  private updateHighlightStatus() {
    this.isHighlighted = this.highlightDirective.isHighlighted();
  }
}
```

## 実践的な活用例
- ツールチップディレクティブの制御
- バリデーションディレクティブの状態確認
- アニメーションディレクティブの操作

## ベストプラクティス
- ディレクティブの公開メソッドを明確にする
- 適切な型定義を使用する
- ディレクティブの状態を適切に管理する

## 注意点
- ディレクティブの存在チェック
- メソッドの呼び出しタイミング
- 副作用の管理

## 関連技術
- カスタムディレクティブ
- ElementRef
- Renderer2
- ディレクティブ設計
