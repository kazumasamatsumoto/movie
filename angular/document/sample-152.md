# #152 「テンプレート参照変数 # の活用」

## 概要
Angular v20におけるテンプレート参照変数の高度な活用方法。#refNameで定義した参照をViewChild、テンプレート内での直接参照、コンポーネント間通信などで効率的に使用する手法を学ぶ。

## 学習目標
- テンプレート参照変数の活用方法を理解する
- 様々な場面での使用例を学ぶ
- 効率的な要素参照を把握する

## 技術ポイント
- テンプレート参照変数の定義
- ViewChildでの参照取得
- テンプレート内での直接参照
- コンポーネント間通信

## 📺 画面表示用コード

### ViewChildでの活用
```typescript
@Component({
  selector: 'app-ref-viewchild',
  template: `
    <input #inputRef type="text" placeholder="入力してください">
    <button (click)="focusInput()">フォーカス</button>
  `
})
export class RefViewChildComponent implements AfterViewInit {
  @ViewChild('inputRef') inputRef!: ElementRef<HTMLInputElement>;

  ngAfterViewInit() {
    console.log('入力要素:', this.inputRef.nativeElement);
  }

  focusInput() {
    this.inputRef.nativeElement.focus();
  }
}
```

### テンプレート内での直接参照
```typescript
@Component({
  selector: 'app-ref-direct',
  template: `
    <div #infoPanel class="panel">
      情報パネル
    </div>
    <button (click)="infoPanel.style.display = 'none'">
      パネル非表示
    </button>
    <button (click)="infoPanel.style.display = 'block'">
      パネル表示
    </button>
  `
})
export class RefDirectComponent {}
```

## 実践的な活用例
- フォーム要素の制御
- モーダルの表示制御
- アニメーション要素の操作

## ベストプラクティス
- 明確で意味のある参照名
- 適切なスコープの使用
- 型安全性の確保

## 注意点
- 参照名の重複回避
- スコープの理解
- パフォーマンスの考慮

## 関連技術
- テンプレート参照変数
- ViewChild
- DOM操作
