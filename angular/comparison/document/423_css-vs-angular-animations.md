# #423 「CSSトランジション vs Angular Animations あなたはどっち派？」

## 概要
CSSトランジションは軽量で汎用的。Angular Animationsは状態管理や複雑なシーケンスに強い。要件に応じて選択する。

## 学習目標
- CSSトランジションの構成と得意なシナリオを整理する
- Angular Animationsの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- CSSトランジションを成り立たせる主要API/構成要素
- Angular Animationsで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**CSS派：クラスにtransitionを仕込む**
```typescript
.card {
  transition: transform 200ms ease;
}
.card:hover {
  transform: translateY(-4px);
}
```

**Angular Animations派：triggerで制御**
```typescript
@Component({
  animations: [
    trigger('fade', [
      transition(':enter', [style({ opacity: 0 }), animate('200ms', style({ opacity: 1 }))]),
      transition(':leave', [animate('200ms', style({ opacity: 0 }))]),
    ]),
  ],
})
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-card',
  standalone: true,
  animations: [
    trigger('highlight', [
      state('active', style({ transform: 'scale(1.02)' })),
      state('rest', style({ transform: 'scale(1)' })),
      transition('rest <=> active', animate('150ms ease-in-out')),
    ]),
  ],
})
export class HeroCardComponent {
  state = signal<'rest' | 'active'>('rest');
}
```

## ベストプラクティス
- CSSトランジションで済む箇所はCSSに寄せ、ロジックを薄く保つ
- Angular Animationsを使う場合はトリガー名/状態名の命名を統一し、Router Animationsとも整合させる
- パフォーマンス計測でアニメーションがメインスレッドを圧迫していないか確認する

## 注意点
- Angular Animationsはランタイムサイズが増えるため必要な箇所だけに絞る
- CSSアニメーションでも`will-change`指定の乱用は避ける
- SSR環境でアニメーションを使用する場合は`BrowserAnimationsModule`導入を忘れない

## 関連技術
- Angular Animations
- CSS transition/keyframes
- BrowserAnimationsModule
