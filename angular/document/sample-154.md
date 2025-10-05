# #154 「ElementRef での直接 DOM アクセス」

## 概要
Angular v20におけるElementRefを使った直接的なDOMアクセス。nativeElementプロパティを介してDOM要素に直接アクセスし、スタイル変更や属性操作を実現する方法を学ぶ。

## 学習目標
- ElementRefの基本的な使い方を理解する
- nativeElementでのDOM操作を学ぶ
- 直接アクセスの実装方法を把握する

## 技術ポイント
- ElementRef.nativeElement でのDOMアクセス
- スタイル変更と属性設定
- DOM要素の直接操作
- 型安全性の確保

## 📺 画面表示用コード

### ElementRefでの直接DOM操作
```typescript
@Component({
  selector: 'app-direct-dom',
  template: `
    <div #targetElement class="target">
      操作対象要素
    </div>
    <div class="controls">
      <button (click)="changeStyle()">スタイル変更</button>
      <button (click)="changeAttribute()">属性変更</button>
      <button (click)="addEventListener()">イベント追加</button>
    </div>
  `
})
export class DirectDomComponent implements AfterViewInit {
  @ViewChild('targetElement') targetElement!: ElementRef<HTMLDivElement>;

  ngAfterViewInit() {
    console.log('DOM要素:', this.targetElement.nativeElement);
  }

  changeStyle() {
    const element = this.targetElement.nativeElement;
    element.style.backgroundColor = 'lightblue';
    element.style.padding = '20px';
    element.style.borderRadius = '10px';
  }

  changeAttribute() {
    const element = this.targetElement.nativeElement;
    element.setAttribute('data-modified', 'true');
    element.setAttribute('title', 'DOM操作済み');
  }

  addEventListener() {
    const element = this.targetElement.nativeElement;
    element.addEventListener('click', () => {
      alert('要素がクリックされました');
    });
  }
}
```

## 実践的な活用例
- 動的なスタイル変更
- カスタムイベントの追加
- DOM要素の直接制御

## ベストプラクティス
- 適切な型定義
- エラーハンドリング
- プラットフォーム非依存の考慮

## 注意点
- セキュリティリスクの考慮
- SSRでの問題
- メモリリークの防止

## 関連技術
- ElementRef
- DOM操作
- 型安全性
