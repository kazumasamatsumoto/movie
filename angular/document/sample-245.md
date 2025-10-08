# #245 「動的 Component のパフォーマンス」

## 概要
動的コンポーネントの生成・破棄によるパフォーマンスへの影響を理解し、最適化のためのテクニック（プール、OnPush、遅延ロードなど）を紹介します。

## 学習目標
- 生成コストやChange Detectionコストを意識した設計を理解する
- コンポーネントの再利用やプールを導入する場面を把握する
- パフォーマンス計測と最適化の流れを習得する

## 技術ポイント
- **生成コスト**: create/destroyを多用するとCPU負荷が高くなる
- **OnPush**: 生成するコンポーネントに`ChangeDetectionStrategy.OnPush`を設定
- **プール**: ComponentRefを再利用し、頻繁な再生成を避ける
- **Lazy loading**: 必要なコンポーネントのみ読み込むことで初期ロードを削減

## 📺 画面表示用コード（動画用）

```typescript
@Component({ changeDetection: ChangeDetectionStrategy.OnPush })
```

```typescript
const ref = pool.length ? pool.pop()! : host.createComponent(WidgetComponent);
```

```typescript
performance.mark('start'); ... performance.measure('generate', 'start');
```

## 💻 詳細実装例（学習用）
```markdown
### 最適化ヒント
1. **OnPush**: 動的生成するコンポーネントにOnPushを設定し、不要なChange Detectionを抑える
2. **プール**: 同種コンポーネントを破棄せずプールへ戻し、再利用（`ref.hostView.detach()`）
3. **Lazy load**: Dynamic importで必要になったタイミングでコンポーネントを読み込む
4. **Batch処理**: 多数生成する場合は`requestAnimationFrame`等で分割し、メインスレッドを塞がない
5. **計測**: `performance.measure`やAngular DevTools Profilerでボトルネックを特定
```

## ベストプラクティス
- 動的生成が大量に発生する場合、プールや仮想スクロールを導入して再利用性を高める
- 生成後すぐに大量のデータをバインドする場合、Change Detectionを手動で制御しフレームを分割する
- パフォーマンス計測を定期的に行い、改善サイクルを回す

## 注意点
- プールを導入する場合は状態リセットを忘れずに行う（旧データが残ると予期せぬ表示になる）
- `detach()`でビューを外すとChange Detectionが止まるため、必要なタイミングで`reattach()`を呼ぶ
- 遅延ロードする場合、bundle分割によるロード遅延とユーザー体験のバランスを取る

## 関連技術
- ComponentRef活用・メモリ管理（#232, #242）
- 遅延ロードコンポーネント（#235）
- Angular DevTools Profilerでの測定
