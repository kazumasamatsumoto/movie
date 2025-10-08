# #217 「コンテンツ投影のテスト」

## 概要
コンテンツ投影を利用したコンポーネントをユニットテストする方法を学び、ホストコンポーネントを介して投影内容を検証する実践的な手法を整理します。

## 学習目標
- TestBedでホストコンポーネントを作成し、投影コンテンツを差し込むテクニックを理解する
- `fixture.detectChanges()`後のDOMを検証して投影が成功しているか確認する
- `ContentChild`/`ContentChildren`の値をテストする方法を習得する

## 技術ポイント
- **ホストコンポーネント**: テスト専用にテンプレートを持つコンポーネントを作り、投影内容を宣言
- **DOMアサーション**: `fixture.nativeElement.querySelector(...)`で描画結果を確認
- **投影API検証**: 期待するセレクタを付け忘れた場合の挙動をテストでカバー

## 📺 画面表示用コード（動画用）

```typescript
@Component({ template: `<app-card><h3 card-header>テスト</h3></app-card>` })
class HostComponent {}
```

```typescript
const header = fixture.nativeElement.querySelector('.card__header h3');
```

```typescript
expect(header?.textContent).toContain('テスト');
```

## 💻 詳細実装例（学習用）
```typescript
// card.component.spec.ts
import { Component } from '@angular/core';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CardComponent } from './card.component';

@Component({
  template: `
    <app-card>
      <h3 card-header>ヘッダー</h3>
      <p>本文テキスト</p>
    </app-card>
  `,
})
class HostComponent {}

describe('CardComponent (Content Projection)', () => {
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardComponent],
      declarations: [HostComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(HostComponent);
    fixture.detectChanges();
  });

  it('should project card-header content into header slot', () => {
    const header: HTMLElement | null = fixture.nativeElement.querySelector('.card__header h3');
    expect(header?.textContent).toContain('ヘッダー');
  });
});
```

## ベストプラクティス
- 投影コンテンツを持つコンポーネントでは、ホストコンポーネントを利用したテストを作成し契約を保証する
- 必須スロットが未指定のケースもテストし、フォールバックが正しく表示されるか確認する
- `ContentChild`/`ContentChildren`を利用するコンポーネントは、参照が取得できているかアサートする

## 注意点
- `fixture.detectChanges()`を忘れると投影が行われず、テストが失敗する
- テストで使用するセレクタが実装依存になりすぎないよう、クラス名や役割に基づいたアサーションを行う
- 重いテンプレートを使用するとテスト実行時間が増えるため、最小限のテスト用マークアップにする

## 関連技術
- Angular Testing Library
- Storybookなどのコンポーネントドキュメントツール
- `ContentChild`ライフサイクル（#206, #207）

