# #267 「Higher Order Component」

## 概要
Higher Order Component（HOC）はコンポーネントを引数として受け取り、新たな振る舞いや依存を付与したコンポーネントを返すパターンである。

## 学習目標
- HOCで依存やUIをラップする方法を理解する
- Generic型を使った型安全なHOCを設計する
- Angular特有のDIと組み合わせる手法を学ぶ

## 技術ポイント
- Standalone Component Factory
- environmentInjectorによるDI拡張
- 型パラメータによるInput継承

## 📺 画面表示用コード（動画用）
```typescript
export type HocComponent<TProps> = Type<TProps>;
```

```typescript
export function withLoading<T>(Component: HocComponent<T>) {
  @Component({ selector: 'hoc-loading', standalone: true, imports: [Component], template: `<ng-container *ngIf="ready"><ng-container *ngComponentOutlet="inner"></ng-container></ng-container>` })
  class LoadingComponent {
    @Input() ready = false;
    protected readonly inner = Component;
  }
  return LoadingComponent;
}
```

```typescript
const WrappedProfile = withLoading(ProfileComponent);
```

## 💻 詳細実装例（学習用）
```typescript
export function withStore<TInputs, TStore>(
  component: HocComponent<TInputs>,
  providers: Provider[]
) {
  @Component({
    selector: 'hoc-store',
    standalone: true,
    imports: [component],
    providers,
    template: `<ng-container *ngComponentOutlet="component"></ng-container>`
  })
  class StoreHocComponent {}
  return StoreHocComponent;
}
```

## ベストプラクティス
- HOCは目的ごとに小さく分け、組み合わせて再利用する
- TypeScriptの型でInput継承を保証し破壊的変更を防ぐ
- providersオプションで追加の依存を明記する

## 注意点
- 過度なネストはスタックトレースを追いにくくするため命名を明示する
- HOCはスタンドアロンコンポーネント同士で適用する
- テスト時は生成されたコンポーネントを直接レンダーして挙動を確認する

## 関連技術
- Standalone Component
- Dependency Injection
- ComponentFactory
