# #156 「Renderer2 での安全な DOM 操作」

## 概要
Angular v20におけるRenderer2を使った安全なDOM操作。プラットフォーム非依存でSSRやWebWorkerでも動作する抽象化されたAPIを使用し、堅牢で移植性の高いDOM操作を実現する方法を学ぶ。

## 学習目標
- Renderer2の基本的な使い方を理解する
- ElementRefとの違いを学ぶ
- 安全なDOM操作を把握する

## 技術ポイント
- Renderer2の抽象化API
- プラットフォーム非依存の実装
- SSR対応
- セキュリティの向上

## 📺 画面表示用コード

### Renderer2での安全なDOM操作
```typescript
@Component({
  selector: 'app-safe-renderer',
  template: `
    <div #targetElement class="target">
      安全なDOM操作対象
    </div>
    <div class="controls">
      <button (click)="safeStyleChange()">安全なスタイル変更</button>
      <button (click)="safeAttributeChange()">安全な属性変更</button>
      <button (click)="safeClassToggle()">クラス切り替え</button>
    </div>
  `
})
export class SafeRendererComponent implements AfterViewInit {
  @ViewChild('targetElement') targetElement!: ElementRef;

  constructor(private renderer: Renderer2) {}

  ngAfterViewInit() {
    console.log('Renderer2準備完了');
  }

  safeStyleChange() {
    // Renderer2を使用した安全なスタイル変更
    this.renderer.setStyle(
      this.targetElement.nativeElement,
      'backgroundColor',
      'lightgreen'
    );
    this.renderer.setStyle(
      this.targetElement.nativeElement,
      'border',
      '2px solid green'
    );
  }

  safeAttributeChange() {
    // Renderer2を使用した安全な属性変更
    this.renderer.setAttribute(
      this.targetElement.nativeElement,
      'data-safe',
      'true'
    );
    this.renderer.setProperty(
      this.targetElement.nativeElement,
      'title',
      'Renderer2で操作済み'
    );
  }

  safeClassToggle() {
    // Renderer2を使用したクラス操作
    this.renderer.addClass(
      this.targetElement.nativeElement,
      'highlight'
    );
  }
}
```

## 実践的な活用例
- プラットフォーム非依存の実装
- SSR対応アプリケーション
- セキュアなDOM操作

## ベストプラクティス
- ElementRefよりRenderer2を優先
- プラットフォーム非依存を意識
- 適切な抽象化レベル

## 注意点
- パフォーマンスの考慮
- 適切なAPI選択
- 将来の互換性

## 関連技術
- Renderer2
- プラットフォーム非依存
- セキュアなDOM操作
