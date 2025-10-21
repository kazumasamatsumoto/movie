# #434 「イベントのシミュレーション」

## 概要
テストでは`dispatchEvent`や`triggerEventHandler`を使ってイベントをシミュレーションし、HostListenerが期待通り動作するか確認する。

## 学習目標
- DOMイベントのシミュレーション方法を理解する
- MouseEvent/KeyboardEventの生成とdispatchを学ぶ
- fakeAsyncやタイマー制御で安定したテストを書く

## 技術ポイント
- `element.dispatchEvent(new Event('click'))`
- `new MouseEvent('mousemove', { clientX: 10 })`
- `fixture.debugElement.triggerEventHandler('click', {})`

## 📺 画面表示用コード（動画用）
```typescript
button.dispatchEvent(new MouseEvent('click'));
```

## 💻 詳細実装例（学習用）
```typescript
it('should handle keydown', () => {
  const fixture = TestBed.createComponent(HostComponent);
  const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
  input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
  fixture.detectChanges();
  expect(...).toBeTrue();
});
```

## ベストプラクティス
- 実際の利用パターンに近いイベントを生成し、プロパティを設定
- タイマー依存の挙動は`fakeAsync`/`tick`で制御し安定化
- グローバルイベント（document/window）は後片付けまでテストする

## 注意点
- `Event`生成時のオプションはブラウザによって挙動が異なることがある
- 多重にイベントを発火するときは`await fixture.whenStable()`を使用
- Jest環境ではDOM APIのサポート状況に注意しPolyfillを導入

## 関連技術
- fakeAsync / tick
- Angular DebugElement
- Jest DOM
