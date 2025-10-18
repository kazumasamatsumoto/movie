# #121 「Input/Output のテスト方法」

## 概要
@Input() / @Output()を利用するコンポーネントのユニットテスト手法を解説します。TestBedを用いてInputを設定し、Outputイベントを検証する方法を学びます。

## 学習目標
- TestBedでコンポーネントを生成し、@Input()を設定する方法を理解する
- EventEmitterのイベント発火を`Observable`として検証する手順を習得する
- テスト時に`fixture.detectChanges()`のタイミングを把握する

## 技術ポイント
- **Input設定**: `fixture.componentInstance.inputProp = value;`
- **detectChanges**: Input反映後に呼び出す
- **Output検証**: `subscribe`または`toPromise`でイベントを捕捉

```typescript
const fixture = TestBed.createComponent(TargetComponent);
```

```typescript
fixture.componentInstance.value = 'test';
fixture.detectChanges();
```

```typescript
fixture.componentInstance.saved.subscribe((value) => expect(value).toBe(true));
```

## 💻 詳細実装例（学習用）
```typescript
// target.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-target',
  standalone: true,
  template: `
    <button type="button" (click)="save()">保存</button>
  `,
})
export class TargetComponent {
  @Input() label = '保存';
  @Output() saved = new EventEmitter<boolean>();

  save(): void {
    this.saved.emit(true);
  }
}
```

```typescript
// target.component.spec.ts
import { TestBed } from '@angular/core/testing';
import { TargetComponent } from './target.component';

describe('TargetComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TargetComponent],
    }).compileComponents();
  });

  it('should render label', () => {
    const fixture = TestBed.createComponent(TargetComponent);
    fixture.componentInstance.label = '送信';
    fixture.detectChanges();
    const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
    expect(button.textContent).toContain('送信');
  });

  it('should emit saved event', (done) => {
    const fixture = TestBed.createComponent(TargetComponent);
    fixture.detectChanges();
    fixture.componentInstance.saved.subscribe((result) => {
      expect(result).toBeTrue();
      done();
    });
    const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
    button.click();
  });
});
```

## ベストプラクティス
- Outputイベントの検証には`subscribe`を用い、非同期テストでは`done()`を利用する
- Input設定後は`detectChanges()`を必ず呼んでテンプレートへ反映させる
- テストの可読性を高めるため、Given/When/Thenパターンで記述する

## 注意点
- Outputテストで`done()`を忘れるとテストがタイムアウトする
- イベントが複数回発火する場合は`take(1)`で一度だけ購読するか、`expect`の回数を指定する
- Standaloneコンポーネントでは`imports`に対象コンポーネントを直接記載する

## 関連技術
- Angular Testing Library
- Jest / Vitest を使う場合のAngularテストセットアップ
- AsyncPipeやObservableを含むコンポーネントのテスト
