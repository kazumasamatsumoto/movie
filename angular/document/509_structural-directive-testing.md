# #509 「カスタム Structural Directive のテスト」

## 概要
カスタムStructural Directiveのテストではホストコンポーネントを作成し、ViewContainerRefの結果やテンプレートの表示状態を確認して期待通りに構造が変化するか検証する。

## 学習目標
- Structural Directiveをテストする手順を理解する
- ホストテンプレートでディレクティブを使用する方法を学ぶ
- ビュー生成・削除やContextの内容をアサートする

## 技術ポイント
- Hostコンポーネントをstandaloneで定義しTestBedにimports
- `fixture.detectChanges()`→`querySelector`でDOM状態確認
- 条件を変化させた後再度`detectChanges`し結果をアサート

## 📺 画面表示用コード（動画用）
```typescript
const host = TestBed.createComponent(HostComponent);
host.componentInstance.condition = false;
host.detectChanges();
```

## 💻 詳細実装例（学習用）
```typescript
describe('UnlessDirective', () => {
  @Component({
    standalone: true,
    imports: [UnlessDirective],
    template: `<p *appUnless="condition">非表示条件</p>`
  })
  class HostComponent {
    condition = false;
  }

  it('should render when condition is false', () => {
    const fixture = TestBed.createComponent(HostComponent);
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('非表示条件');
  });

  it('should remove view when condition is true', () => {
    const fixture = TestBed.createComponent(HostComponent);
    fixture.componentInstance.condition = true;
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent.trim()).toBe('');
  });
});
```

## ベストプラクティス
- Hostコンポーネントをスタンドアロン化しシンプルに保つ
- 条件変更を複数回実行しビューの生成・破棄を検証
- Contextに渡した値は`DebugElement`から`context`を参照して確認

## 注意点
- DOMテキストのアサートは余分な空白をtrimする
- 非同期ディレクティブは`fakeAsync`/`tick`や`waitForAsync`を使用
- TestBedの状態は各テストで共有されるため初期化に留意

## 関連技術
- Angular TestBed
- DebugElement
- Structural Directiveテストパターン
