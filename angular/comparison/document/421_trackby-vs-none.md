# #421 「ngFor trackBy無し vs trackBy導入 あなたはどっち派？」

## 概要
trackByなしは楽だが差分レンダリングができずパフォーマンスが劣る。trackByは少しのコードでUXが向上する。

## 学習目標
- trackByなしの構成と得意なシナリオを整理する
- trackByありの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- trackByなしを成り立たせる主要API/構成要素
- trackByありで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**trackByなし：そのままループ**
```typescript
<li *ngFor="let hero of heroes">{{ hero.name }}</li>
```

**trackByあり：キーで追跡**
```typescript
<li *ngFor="let hero of heroes; trackBy: trackById">
  {{ hero.name }}
</li>

trackById(_: number, hero: Hero) {
  return hero.id;
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-hero-list',
  standalone: true,
  templateUrl: './hero-list.component.html',
})
export class HeroListComponent {
  readonly heroes = signal<Hero[]>([]);

  trackById(_: number, hero: Hero) {
    return hero.id;
  }
}
```

## ベストプラクティス
- IDがあるリストは必ずtrackByを定義し、Signals/Observablesの更新に備える
- 配列の順序が頻繁に変わる場合はtrackByでもDOM再使用があるため、Keyの安定性を確認する
- コード生成ツールにもtrackByテンプレを組み込み、書き忘れを防ぐ

## 注意点
- trackByが重い計算をすると逆にパフォーマンスを落とすため関数を軽量に保つ
- ユニークキーがない場合にindexを返すと効果がなくなる
- trackBy関数でオブジェクトを返すと参照が毎回変わり再描画が止まらない

## 関連技術
- *ngFor
- trackBy
- 変更検知最適化
