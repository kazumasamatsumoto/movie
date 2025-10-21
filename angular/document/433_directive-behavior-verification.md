# #433 「Directive の動作確認」

## 概要
ディレクティブの動作確認はDOM変化、属性更新、イベント通知など仕様で求められる挙動をテストで確認し、リグレッションを防ぐ。

## 学習目標
- アサーションの対象を明確にする方法を理解する
- DOMとクラス/スタイルの検証技法を学ぶ
- Outputイベントの検証方法を把握する

## 技術ポイント
- `classList.contains`, `getAttribute`で結果を検証
- `spyOn`でEventEmitterの`emit`呼び出しを確認
- `fixture.detectChanges()`で更新を適用

## 📺 画面表示用コード（動画用）
```typescript
expect(button.classList.contains('is-active')).toBeTrue();
```

## 💻 詳細実装例（学習用）
```typescript
it('should emit toggle event', () => {
  const fixture = TestBed.createComponent(HostComponent);
  const directive = fixture.debugElement.query(By.directive(ToggleDirective)).injector.get(ToggleDirective);
  const spy = spyOn(directive.appToggle, 'emit');
  const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
  button.click();
  expect(spy).toHaveBeenCalledWith(true);
});
```

## ベストプラクティス
- 仕様書に基づいてアサーション項目を列挙し、テストに反映
- DOMとイベントの両面から挙動を検証し、回 regressions を防止
- テストは可能な限り独立させ、外部状態に依存しないようにする

## 注意点
- 仕様変更時にテストも適切に更新し、実装との乖離を防ぐ
- CSSによる見た目はユニットテストではなくStorybookなどで確認する
- 複雑なタイミングが絡む場合はfakeAsync/tickを利用

## 関連技術
- Jasmine/Jest matchers
- Angular Testing Library
- Storybook Visualテスト
