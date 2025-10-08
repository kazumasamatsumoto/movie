# #096 「@Input() 型定義とバリデーション」

## 概要
@Input()プロパティに適切な型注釈を付け、必要に応じてバリデーションを行うことで、予期しない値の流入を防ぐ方法を学びます。

## 学習目標
- TypeScript型で@Input()の契約を明示する
- setterやngOnChangesを使ってバリデーションする
- ランタイム検証ライブラリを併用するケースを把握する

## 技術ポイント
- **型注釈**: `@Input() count!: number;`
- **setterガード**: `set config(value: Config) { assertValid(value); }`
- **スキーマ検証**: zodやclass-validatorでのランタイムチェック

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() maxItems = 10;
```

```typescript
@Input()
set config(value: ChartConfig) {
  if (!value.series?.length) throw new Error('seriesは必須です');
  this._config = value;
}
```

```typescript
type ChartConfig = { title: string; series: number[] };
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input } from '@angular/core';
import { z } from 'zod';

const ChartConfigSchema = z.object({
  title: z.string(),
  series: z.array(z.number()).nonempty(),
});

type ChartConfig = z.infer<typeof ChartConfigSchema>;

@Component({
  selector: 'app-chart-card',
  standalone: true,
  templateUrl: './chart-card.component.html',
})
export class ChartCardComponent {
  private _config: ChartConfig = { title: '未設定', series: [0] };

  @Input({ required: true })
  set config(value: ChartConfig) {
    this._config = ChartConfigSchema.parse(value);
  }
  get config(): ChartConfig {
    return this._config;
  }

  @Input()
  maxItems = 10;
}
```

```html
<!-- chart-card.component.html -->
<section class="chart-card">
  <h3>{{ config.title }}</h3>
  <ul>
    <li @for (value of config.series.slice(0, maxItems); track value)">
      {{ value }}
    </li>
  </ul>
</section>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { ChartCardComponent } from './chart-card.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [ChartCardComponent],
  template: `
    <app-chart-card
      [config]="chartConfig"
      [maxItems]="5"
    ></app-chart-card>
  `,
})
export class DashboardComponent {
  chartConfig = {
    title: 'PV推移',
    series: [120, 150, 180, 210],
  };
}
```

## ベストプラクティス
- @Input()には必ず型を付け、ドキュメントなしでも意図が伝わるようにする
- setterでのバリデーションは軽量に保ち、重い処理はサービスに委譲する
- バリデーションエラーをthrowする場合は、コンソールに詳細を出して原因を調査しやすくする

## 注意点
- バリデーションで例外を投げるとコンポーネント作成が失敗するため、UIが崩れないよう防御的に扱う
- zodなどランタイム依存を追加する場合はバンドルサイズへの影響を考慮する
- setter内でSignalやStateを更新する際は無限ループを避けるため条件を設ける

## 関連技術
- TypeScriptユニオン型での制約
- Angular Signalsと組み合わせた型安全な状態管理
- ESLint `@angular-eslint/no-inputs-metadata-property`
