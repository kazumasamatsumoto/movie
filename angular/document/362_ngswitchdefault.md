# #362 「*ngSwitchDefault - デフォルト」

## 概要
`*ngSwitchDefault`はどのケースにも一致しない場合に表示されるフォールバックで、予期しない状態をユーザーに知らせる役割を持つ。

## 学習目標
- defaultケースの重要性を理解する
- 例外時のメッセージ設計を学ぶ
- ロギングやエラーハンドリングとの連携を想定する

## 技術ポイント
- `*ngSwitchDefault`は1つの`ngSwitch`ブロックにつき0個または1個
- defaultでもテンプレート参照を使い共通化が可能
- フィードバックだけでなく、復旧手段を提供するとUXが向上

## 📺 画面表示用コード（動画用）
```html
<p *ngSwitchDefault>サポートされていない状態です。</p>
```

## 💻 詳細実装例（学習用）
```typescript
type Mode = 'view' | 'edit';

@Component({
  selector: 'app-switch-default-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngSwitch]="mode">
      <p *ngSwitchCase="'view'">閲覧モード</p>
      <p *ngSwitchCase="'edit'">編集モード</p>
      <p *ngSwitchDefault>未知のモードです。サポートへ連絡してください。</p>
    </div>
  `
})
export class SwitchDefaultDemoComponent {
  protected mode: Mode | 'unknown' = 'unknown';
}
```

## ベストプラクティス
- defaultでログ出力やSentry通知など運用上のアクションを取れるようにする
- ユーザーが次に取るべき行動をボタンやリンクで提示する
- テストでdefaultが発火するケースを確認し、期待した文言が表示されるか検証する

## 注意点
- defaultを用意しないと何も表示されず障害が気付きづらくなる
- default自体が複雑になりすぎないようにシンプルに保つ
- 状態が増えた際にdefaultが不要になった場合は忘れず更新する

## 関連技術
- Error Handling
- Logging
- UX Writing
