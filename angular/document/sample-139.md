# #139 「ViewChild で DOM 操作」

## 概要
Angular v20におけるViewChildを使ったDOM操作の実装方法。ElementRefのnativeElementを介してDOM要素に直接アクセスし、スタイル変更、属性設定、イベントリスナーの追加などの操作を実現する方法を学ぶ。

## 学習目標
- ViewChildでのDOM操作の基本を理解する
- ElementRefの使用方法を学ぶ
- 安全なDOM操作の実装方法を把握する

## 技術ポイント
- ElementRef.nativeElement でのDOMアクセス
- スタイル変更と属性設定
- イベントリスナーの追加・削除
- プラットフォーム非依存な実装

## 📺 画面表示用コード

### 基本的なDOM操作
```typescript
@Component({
  selector: 'app-dom-manipulation',
  template: `
    <div #targetElement class="target">
      DOM操作対象要素
    </div>
    <div class="controls">
      <button (click)="changeStyle()">スタイル変更</button>
      <button (click)="changeAttribute()">属性変更</button>
      <button (click)="addEventListener()">イベント追加</button>
      <button (click)="removeEventListener()">イベント削除</button>
    </div>
  `,
  styles: [`
    .target {
      padding: 20px;
      border: 1px solid #ccc;
      margin: 10px 0;
      transition: all 0.3s ease;
    }
    .highlight {
      background-color: yellow;
      border-color: orange;
    }
  `]
})
export class DomManipulationComponent implements AfterViewInit, OnDestroy {
  @ViewChild('targetElement') targetElement!: ElementRef<HTMLDivElement>;
  
  private clickListener?: () => void;
  
  ngAfterViewInit() {
    console.log('DOM操作準備完了');
  }
  
  changeStyle() {
    const element = this.targetElement.nativeElement;
    element.style.backgroundColor = 'lightblue';
    element.style.padding = '30px';
    element.style.borderRadius = '10px';
  }
  
  changeAttribute() {
    const element = this.targetElement.nativeElement;
    element.setAttribute('data-modified', 'true');
    element.setAttribute('title', 'DOM操作済み要素');
  }
  
  addEventListener() {
    const element = this.targetElement.nativeElement;
    this.clickListener = () => {
      element.classList.toggle('highlight');
    };
    element.addEventListener('click', this.clickListener);
  }
  
  removeEventListener() {
    if (this.clickListener) {
      this.targetElement.nativeElement.removeEventListener('click', this.clickListener);
      this.clickListener = undefined;
    }
  }
  
  ngOnDestroy() {
    // クリーンアップ
    this.removeEventListener();
  }
}
```

### Renderer2を使った安全なDOM操作
```typescript
@Component({
  selector: 'app-safe-dom',
  template: `
    <div #safeElement class="safe-target">
      安全なDOM操作要素
    </div>
    <div class="controls">
      <button (click)="safeStyleChange()">安全なスタイル変更</button>
      <button (click)="safeAttributeChange()">安全な属性変更</button>
      <button (click)="safeClassToggle()">クラス切り替え</button>
    </div>
  `,
  styles: [`
    .safe-target {
      padding: 15px;
      border: 1px solid #ddd;
      margin: 10px 0;
    }
    .active {
      background-color: lightgreen;
      color: darkgreen;
    }
  `]
})
export class SafeDomComponent implements AfterViewInit {
  @ViewChild('safeElement') safeElement!: ElementRef<HTMLDivElement>;
  
  constructor(private renderer: Renderer2) {}
  
  ngAfterViewInit() {
    console.log('安全なDOM操作準備完了');
  }
  
  safeStyleChange() {
    // Renderer2を使用した安全なスタイル変更
    this.renderer.setStyle(
      this.safeElement.nativeElement,
      'backgroundColor',
      'lightcoral'
    );
    this.renderer.setStyle(
      this.safeElement.nativeElement,
      'border',
      '2px solid red'
    );
  }
  
  safeAttributeChange() {
    // Renderer2を使用した安全な属性変更
    this.renderer.setAttribute(
      this.safeElement.nativeElement,
      'data-safe',
      'true'
    );
    this.renderer.setProperty(
      this.safeElement.nativeElement,
      'title',
      'Renderer2で操作済み'
    );
  }
  
  safeClassToggle() {
    // Renderer2を使用したクラス操作
    this.renderer.addClass(
      this.safeElement.nativeElement,
      'active'
    );
  }
}
```

## 実践的な活用例
- 動的なスタイル変更
- カスタムアニメーション
- フォーカス制御
- 要素の表示・非表示制御

## ベストプラクティス
- Renderer2の使用を推奨
- 適切なクリーンアップを実装
- プラットフォーム非依存な実装
- パフォーマンスを考慮する

## 注意点
- nativeElementの直接操作は最小限に
- イベントリスナーの適切な削除
- メモリリークの防止
- SSRでの考慮

## 関連技術
- ElementRef
- Renderer2
- DOM操作
- プラットフォーム非依存
