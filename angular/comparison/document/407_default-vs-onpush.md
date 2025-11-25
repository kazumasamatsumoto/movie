# #407 「ChangeDetection Default vs OnPush あなたはどっち派？」

## 概要
ChangeDetection Defaultは使いやすいが余計な検知が増える。OnPushは管理コストが上がる代わりにパフォーマンスが安定するため、チームの運用力に合わせて選ぶ。

## 学習目標
- Default戦略の構成と得意なシナリオを整理する
- OnPush戦略の採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- Default戦略を成り立たせる主要API/構成要素
- OnPush戦略で押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**Default：宣言不要で自動検知**
```typescript
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  counter = 0;

  incrementLater() {
    setTimeout(() => this.counter++, 1000);
  }
}
```

**OnPush：必要なタイミングだけ検知**
```typescript
@Component({
  selector: 'app-dashboard',
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  readonly counter = signal(0);

  incrementLater() {
    setTimeout(() => this.counter.update(v => v + 1), 1000);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-score-card',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <h4>{{ score() }}</h4>
    <button (click)="increase()">+1</button>
  `,
})
export class ScoreCardComponent {
  readonly score = signal(0);

  increase(): void {
    this.score.update((v) => v + 1);
  }
}
```

## ベストプラクティス
- Default戦略は検証用や小規模画面に限定し、主要画面はOnPushで統一する
- OnPush採用時は不変データとSignalsをセットで使い、`markForCheck`乱用を避ける
- プロジェクトルールとしてどこにどの戦略を使うかドキュメント化する

## 注意点
- OnPushでMutableオブジェクトを渡すと更新に気づかないので必ずコピーする
- Default戦略はゾーン外の非同期処理で変化が伝わらないケースがある
- ChangeDetectionの混在はバグ源になるのでルールなしに混ぜない

## 関連技術
- ChangeDetectionStrategy
- Signalベース更新
- markForCheck/detectChanges
