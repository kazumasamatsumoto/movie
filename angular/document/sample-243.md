# #243 「動的 Component のテスト」

## 概要
動的コンポーネントをテストする手法を整理し、TestBedとホストコンポーネントを利用して生成・入力・イベントの挙動を検証します。

## 学習目標
- ViewContainerRefを使った動的生成をテストで再現する流れを理解する
- ComponentRef.instanceへの入力設定やイベント購読を検証する
- destroy後の状態をテストし、リーク防止策を確認する

## 技術ポイント
- **ホストコンポーネント**: テスト用テンプレートで`ViewContainerRef`を取得
- **createComponent**: テスト内でコンポーネントを生成し、Input/Outputをアサート
- **クリーンアップ**: `fixture.destroy()`または`ref.destroy()`で後始末

## 📺 画面表示用コード（動画用）

```typescript
const ref = host.createComponent(AlertComponent);
ref.instance.message = 'test';
fixture.detectChanges();
```

```typescript
ref.instance.closed.subscribe(() => closed = true);
```

```typescript
ref.destroy();
```

## 💻 詳細実装例（学習用）
```typescript
// dynamic-host.test-component.ts
import { Component, ViewChild, ViewContainerRef } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({
  template: `<ng-container #host></ng-container>`,
  standalone: true,
  imports: [AlertComponent],
})
export class DynamicHostTestComponent {
  @ViewChild('host', { read: ViewContainerRef, static: true })
  host!: ViewContainerRef;
}
```

```typescript
// alert.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DynamicHostTestComponent } from './dynamic-host.test-component';
import { AlertComponent } from './alert.component';

describe('AlertComponent (dynamic)', () => {
  let fixture: ComponentFixture<DynamicHostTestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DynamicHostTestComponent],
    }).compileComponents();
    fixture = TestBed.createComponent(DynamicHostTestComponent);
    fixture.detectChanges();
  });

  it('should render message when created dynamically', () => {
    const ref = fixture.componentInstance.host.createComponent(AlertComponent);
    ref.instance.message = 'Dynamic Test';
    fixture.detectChanges();
    expect(fixture.nativeElement.textContent).toContain('Dynamic Test');
  });
});
```

## ベストプラクティス
- ホストコンポーネントを用意し、動的生成をテスト内で再現する
- `createComponent`後にInputをセットし、`fixture.detectChanges()`で描画結果を確認する
- `ref.destroy()`や`fixture.destroy()`でテスト終了時にクリーンアップする
- Outputのイベントを購読し、想定したデータが流れるかアサートする

## 注意点
- TestBedにスタンドアロンコンポーネントをインポートすることを忘れない
- `fixture.detectChanges()`を呼ばないと描画が更新されない場合がある
- 生成したComponentRefを配列などに保持すると、テスト終了後に参照が残りやすいのでクリアする

## 関連技術
- 動的コンポーネント生成（#225）
- 動的イベント購読（#227）
- Angular Testing Library / Harnessesによるテスト
