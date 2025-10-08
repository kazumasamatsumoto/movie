# #088 「Lifecycle のテスト方法」

## 概要
Lifecycle Hooksの挙動をユニットテストで検証し、フック内の処理が意図通り実行されることを確認する手法を学びます。

## 学習目標
- TestBedでLifecycleを有効にする方法を理解する
- `fixture.detectChanges()`や`fixture.destroy()`でフックをトリガーする
- `spyOn`やテスト用スタブでフック内部の処理を検証する

## 技術ポイント
- **初期化テスト**: `fixture.detectChanges()`で`ngOnInit`等が呼ばれる
- **破棄テスト**: `fixture.destroy()`または`fixture.componentInstance.ngOnDestroy()`で確認
- **spyOn**: フック実装やサービス呼び出しを監視

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
const fixture = TestBed.createComponent(TargetComponent);
```

```typescript
fixture.detectChanges();
```

```typescript
fixture.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-target',
  standalone: true,
  template: `<p>{{ initialized }}</p>`,
})
export class TargetComponent implements OnInit, OnDestroy {
  initialized = false;
  destroyed = false;

  ngOnInit(): void {
    this.initialized = true;
  }

  ngOnDestroy(): void {
    this.destroyed = true;
  }
}
```

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TargetComponent } from './target.component';

describe('TargetComponent lifecycle', () => {
  let fixture: ComponentFixture<TargetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TargetComponent],
    }).compileComponents();
    fixture = TestBed.createComponent(TargetComponent);
  });

  it('should run ngOnInit on detectChanges', () => {
    fixture.detectChanges();
    expect(fixture.componentInstance.initialized).toBeTrue();
  });

  it('should run ngOnDestroy on destroy', () => {
    fixture.detectChanges();
    fixture.destroy();
    expect(fixture.componentInstance.destroyed).toBeTrue();
  });
});
```

## ベストプラクティス
- `detectChanges`呼び出し前に`componentInstance`へアクセスして初期状態を確認する
- `fakeAsync`や`tick()`を使うと、フック内のタイマー処理をテストできる
- サービス呼び出しを`spyOn`し、Lifecycleで一度だけ実行されることをアサートする

## 注意点
- `TestBed.createComponent`するとconstructorは呼ばれるが、`ngOnInit`は`detectChanges`まで実行されない
- `fixture.destroy()`後に`componentInstance`へアクセスするとエラーになるため注意
- `ngOnDestroy`をテストする際は、AsyncPipeのようなテンプレート購読も破棄されるか確認する

## 関連技術
- Angular Testing Library
- `fakeAsync`, `tick`, `flush`
- JestやVitestでのAngularテストランナー
