# #431 「Directive のテスト」

## 概要
ディレクティブのテストはホストコンポーネントを用意して挙動を検証し、イベント発火やDOM変更が期待通りか確認することで信頼性を高める。

## 学習目標
- ディレクティブテストの基本手順を理解する
- TestBedを用いたセットアップ方法を学ぶ
- DOMアサーションやイベント発火の検証方法を把握する

## 技術ポイント
- ホストコンポーネントを作成しTestBedでレンダリング
- `fixture.detectChanges()`で更新、`fixture.nativeElement`でDOM取得
- `dispatchEvent`でイベントシミュレーション

## 📺 画面表示用コード（動画用）
```typescript
@Component({ template: `<button appToggle>btn</button>` })
class HostComponent {}
```

## 💻 詳細実装例（学習用）
```typescript
describe('ToggleDirective', () => {
  @Component({
    standalone: true,
    imports: [ToggleDirective],
    template: `<button appToggle>Toggle</button>`
  })
  class HostComponent {}

  beforeEach(() => TestBed.configureTestingModule({ imports: [HostComponent] }).compileComponents());

  it('should toggle class on click', () => {
    const fixture = TestBed.createComponent(HostComponent);
    fixture.detectChanges();
    const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
    button.click();
    fixture.detectChanges();
    expect(button.classList.contains('is-active')).toBe(true);
  });
});
```

## ベストプラクティス
- ホストコンポーネントをスタンドアロン化してシンプルに保つ
- イベントシミュレーション後は必ず`detectChanges`を呼ぶ
- Renderer2やOutputの呼び出しをSpyし、期待通りか確認する

## 注意点
- DOM APIの違いでテストが不安定にならないよう、最大限シンプルな検証にする
- グローバルイベントを扱うディレクティブは解除処理もテストする
- Async動作がある場合は`fakeAsync`や`waitForAsync`で制御

## 関連技術
- Angular TestBed
- Testing Library
- Jest/Jasmine
