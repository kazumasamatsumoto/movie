# #226 「動的 Component への入力渡し」

## 概要
動的に生成したコンポーネントへ`@Input`値を渡す方法を整理し、ComponentRef経由でプロパティを設定して表示内容を更新します。

## 学習目標
- ComponentRef.instance経由で`@Input`を設定する手順を理解する
- 入力設定後にChange Detectionを反映させる方法を習得する
- 複数プロパティをまとめて渡す設計を学ぶ

## 技術ポイント
- **入力設定**: `ref.instance.title = '...';`
- **Change Detection**: `ref.changeDetectorRef.detectChanges()`で即時反映
- **複合データ**: Inputをオブジェクトにまとめて渡すと管理しやすい

## 📺 画面表示用コード（動画用）

```typescript
const ref = this.host.createComponent(MessageComponent);
ref.instance.title = '通知';
ref.instance.body = '内容';
ref.changeDetectorRef.detectChanges();
```

```typescript
ref.instance.config = { title: '...', body: '...' };
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-input.component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { MessageComponent } from './message.component';

@Component({
  selector: 'app-dynamic-input',
  standalone: true,
  imports: [MessageComponent],
  templateUrl: './dynamic-input.component.html',
})
export class DynamicInputComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;

  show() {
    this.host.clear();
    const ref = this.host.createComponent(MessageComponent);
    ref.instance.title = 'Hello';
    ref.instance.body = 'Input経由で設定されました';
    ref.changeDetectorRef.detectChanges();
  }
}
```

```typescript
// message.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-message',
  standalone: true,
  template: `
    <article class="message">
      <h3>{{ title }}</h3>
      <p>{{ body }}</p>
    </article>
  `,
})
export class MessageComponent {
  @Input() title = '';
  @Input() body = '';
}
```

## ベストプラクティス
- Inputをまとめた構造体（Configオブジェクト）を定義し、一括で渡すと拡張しやすい
- 生成直後の設定が多い場合は、専用の初期化メソッドをコンポーネント側に用意する
- 入力値の型を明確にし、Optional値にはデフォルトを持たせる

## 注意点
- `detectChanges()`を呼ばないと、Change Detectionサイクルまで表示が更新されない場合がある
- 生成後にInputを変更する場合、`ref.instance`経由で再設定し、必要なら再描画する
- Inputが@Outputと連動する場合はイベント購読の順序に注意する

## 関連技術
- ComponentRef（#232）
- 動的イベント購読（#227）
- 動的コンポーネントのベストプラクティス（#248）
