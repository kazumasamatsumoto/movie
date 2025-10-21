# #432 「TestBed での設定」

## 概要
TestBedではスタンドアロンディレクティブを`imports`に、ホストコンポーネントを`declarations`または`imports`に登録してテスト環境を構築する。

## 学習目標
- TestBed設定の書式を理解する
- スタンドアロンディレクティブの設定方法を学ぶ
- 依存モジュールやサービスのモック方法を把握する

## 技術ポイント
- `TestBed.configureTestingModule({ imports: [HostComponent] })`
- `providers`でサービスモックを提供
- `overrideDirective`で依存ディレクティブを差し替え可能

## 📺 画面表示用コード（動画用）
```typescript
TestBed.configureTestingModule({ imports: [HostComponent] }).compileComponents();
```

## 💻 詳細実装例（学習用）
```typescript
beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [HostComponent],
    providers: [{ provide: TooltipService, useClass: TooltipServiceMock }]
  }).compileComponents();
});
```

## ベストプラクティス
- スタンドアロン構成では`imports`にホストコンポーネントを登録するだけでよい
- サービス依存は`providers`でモックしテストの独立性を保つ
- `compileComponents()`は`beforeEach`で1回だけ呼びキャッシュを活用

## 注意点
- 共有モジュールに依存する場合は追加で`imports`に列挙
- TestBedの状態はテスト間で共有されるため`resetTestingModule`が必要か検討
- `NoopAnimationsModule`などテスト用モジュールを忘れず登録

## 関連技術
- Angular TestBed
- Standalone Components
- Dependency Injection
