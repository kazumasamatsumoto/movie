# #395 「ngComponentOutlet - 動的コンポーネント」

## 概要
`ngComponentOutlet`はコンポーネントクラスを動的に指定してレンダリングできるディレクティブで、プラグインアーキテクチャやCMS構築に向いている。

## 学習目標
- `ngComponentOutlet`の基本的な使い方を理解する
- Injectorや依存関係を差し替える方法を学ぶ
- 動的コンポーネントのパフォーマンス上の注意点を把握する

## 技術ポイント
- `[ngComponentOutlet]="componentType"`で動的生成
- `ngComponentOutletInjector`, `ngComponentOutletContent`, `ngComponentOutletNgModuleFactory`で依存を指定可能
- Standaloneコンポーネントを動的生成する場合は特別なNgModule不要

## 📺 画面表示用コード（動画用）
```html
<ng-container [ngComponentOutlet]="currentComponent"></ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dynamic-host',
  standalone: true,
  imports: [CommonModule, AlertCardComponent, InfoCardComponent],
  template: `
    <button (click)="toggle()">切り替え</button>
    <ng-container [ngComponentOutlet]="component"></ng-container>
  `
})
export class DynamicHostComponent {
  protected component: Type<unknown> = AlertCardComponent;
  protected toggle(): void {
    this.component = this.component === AlertCardComponent ? InfoCardComponent : AlertCardComponent;
  }
}
```

## ベストプラクティス
- コンポーネント一覧をディクショナリ化し、キーからマッピングする
- Injectorを差し替える場合は`EnvironmentInjector`を利用するとスタンドアロン構成でも柔軟
- 動的生成するコンポーネントは`OnPush`やSignalsでパフォーマンスを最適化する

## 注意点
- コンポーネントクラスをバンドルに含める必要があるため、lazy-loadやCDN配信は別途工夫が必要
- 頻繁に切り替えると再生成コストが高くなるためキャッシュを検討
- セキュリティ上、ユーザー入力で直接コンポーネントを指定しないこと

## 関連技術
- Dynamic Component Loader
- EnvironmentInjector
- Router lazy loading
