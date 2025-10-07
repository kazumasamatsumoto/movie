# #021 「Angular DevTools で Component 確認」

## 概要
Angular DevToolsはComponentの状態を可視化し、デバッグを効率化するChrome拡張機能です。

## 学習目標
- Angular DevToolsの基本操作を習得する
- Component階層の確認方法を学ぶ
- プロファイリング機能を理解する

## 技術ポイント
- **Component Explorer**: 階層とプロパティの可視化
- **Profiler**: 変更検知のパフォーマンス分析
- **Injector Tree**: DIの依存関係確認

## 📺 画面表示用コード（動画用）

```bash
# インストール
1. Chrome Web Storeで "Angular DevTools" を検索
2. 拡張機能をインストール
3. F12で開発者ツールを開く
4. "Angular"タブを選択
```

```typescript
// DevToolsで確認できるComponent
@Component({
  selector: 'app-user',
  standalone: true,
  template: '<p>{{name}}</p>'
})
export class UserComponent {
  name = 'John';  // DevToolsで値を確認・編集可能
}
```

```typescript
// 変更検知のプロファイリング
@Component({
  selector: 'app-list',
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class ListComponent {
  @Input() items: Item[] = [];
  // Profilerで変更検知の頻度を確認
}
```

## 💻 詳細実装例（学習用）

### Component Explorerの使用
- Component階層を視覚的に確認
- 各Componentのプロパティをリアルタイム編集
- Input/Outputの値を監視

### Profilerの活用
- 変更検知の実行回数を測定
- パフォーマンスボトルネックを特定
- OnPush戦略の効果を確認

## ベストプラクティス

1. **開発中は常に起動**: バグの早期発見
2. **Profilerで最適化**: パフォーマンス改善
3. **値の確認**: console.logの代替として使用

## 注意点

- 本番ビルドでは使用不可
- 大規模アプリでは動作が重くなる場合あり
- Angular v12以降で利用可能

## 関連技術
- Chrome DevTools
- Performance Profiling
- Change Detection
- Debugging Tools
