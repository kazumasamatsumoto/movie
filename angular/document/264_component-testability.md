# #264 「Component のテスト容易性」

## 概要
テスト容易性の高いコンポーネントは、依存を外部化し純粋なInput/Output契約で構成することで、ユニットテストやコンポーネントハーネスによる検証が容易になる。

## 学習目標
- 依存をInput/Output化してモックしやすくする方法を学ぶ
- OnPush設定による副作用削減を理解する
- Harnessを使ったDOM操作テストを体験する

## 技術ポイント
- Standalone + OnPush構成
- Angular Component Harness
- Test Data Builderパターン

## 📺 画面表示用コード（動画用）
```typescript
@Component({
  selector: 'app-alert',
  standalone: true,
  template: `<div role="alert">{{ message }}</div>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class AlertComponent {
  @Input({ required: true }) message = '';
}
```

```typescript
export const createAlertVm = (message = 'OK') => ({ message });
```

```typescript
export class AlertHarness extends ComponentHarness {
  static hostSelector = 'app-alert';
  async getMessage(): Promise<string> {
    return (await this.locatorFor('div')()).text();
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
describe('AlertComponent', () => {
  it('renders message', async () => {
    await render(AlertComponent, {
      componentInputs: createAlertVm('完了'),
    });

    expect(screen.getByRole('alert').textContent).toBe('完了');
  });
});
```

## ベストプラクティス
- 依存はInput/Outputや抽象サービスに置き換えてモックを容易にする
- HarnessでDOM操作を抽象化しテストの安定性を高める
- Test Data Builderで入力データの生成を共通化する

## 注意点
- コンポーネント内部で`setTimeout`などの副作用を増やさない
- Harnessを作る際はセレクターを安定させる
- renderユーティリティを使う場合は非同期処理を待機する

## 関連技術
- Angular Testing Library
- Component Harness
- OnPush戦略
