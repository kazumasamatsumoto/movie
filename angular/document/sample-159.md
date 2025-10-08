# #159 「ViewChild/ContentChild のテスト」

## 概要
`@ViewChild`や`@ContentChild`を利用するコンポーネントのテスト手法を紹介し、参照が正しく取得できているか検証する方法を学びます。

## 学習目標
- ViewChild参照を持つコンポーネントをTestBedで検証する手順を理解する
- ContentChildのテストにホストコンポーネントを利用する方法を習得する
- ライフサイクルとdetectChangesの関係を把握する

## 技術ポイント
- **ViewChildテスト**: `fixture.detectChanges()`後に`component.child`を検証
- **ContentChildテスト**: 投影用ホストコンポーネントを作成
- **ライフサイクル**: `ngAfterViewInit`/`ngAfterContentInit`が呼ばれるタイミングを考慮

## 📺 画面表示用コード（動画用）

```typescript
const fixture = TestBed.createComponent(TargetComponent);
```

```typescript
fixture.detectChanges();
```

```typescript
expect(fixture.componentInstance.child).toBeTruthy();
```

## 💻 詳細実装例（学習用）
```typescript
// target.component.ts
import { AfterViewInit, Component, ViewChild } from '@angular/core';

@Component({
  selector: 'app-target',
  standalone: true,
  template: `
    <span #label>ViewChildテスト</span>
  `,
})
export class TargetComponent implements AfterViewInit {
  @ViewChild('label') label?: ElementRef<HTMLSpanElement>;
  initialized = false;

  ngAfterViewInit(): void {
    this.initialized = !!this.label;
  }
}
```

```typescript
// target.component.spec.ts
import { ElementRef } from '@angular/core';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TargetComponent } from './target.component';

describe('TargetComponent', () => {
  let fixture: ComponentFixture<TargetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TargetComponent],
    }).compileComponents();
    fixture = TestBed.createComponent(TargetComponent);
    fixture.detectChanges();
  });

  it('should have ViewChild reference', () => {
    expect(fixture.componentInstance.label).toBeInstanceOf(ElementRef);
    expect(fixture.componentInstance.initialized).toBeTrue();
  });
});
```

```typescript
// content-target.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-content-target',
  standalone: true,
  template: `
    <ng-content></ng-content>
  `,
})
export class ContentTargetComponent implements AfterContentInit {
  @ContentChild('projected')
  projected?: TemplateRef<unknown>;
  hasProjection = false;

  ngAfterContentInit(): void {
    this.hasProjection = !!this.projected;
  }
}
```

```typescript
// content-target.component.spec.ts
import { Component } from '@angular/core';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ContentTargetComponent } from './content-target.component';

@Component({
  template: `
    <app-content-target>
      <ng-template #projected>
        <p>投影コンテンツ</p>
      </ng-template>
    </app-content-target>
  `,
})
class HostComponent {}

describe('ContentTargetComponent', () => {
  let fixture: ComponentFixture<HostComponent>;
  let target: ContentTargetComponent;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ContentTargetComponent],
      declarations: [HostComponent],
    }).compileComponents();
    fixture = TestBed.createComponent(HostComponent);
    fixture.detectChanges();
    target = fixture.debugElement.children[0].componentInstance;
  });

  it('should detect projected content', () => {
    expect(target.hasProjection).toBeTrue();
  });
});
```

## ベストプラクティス
- ViewChildをテストする際は`fixture.detectChanges()`を忘れずに呼び出し、ライフサイクルを進める
- ContentChildのテストはホストコンポーネントを用意し、`ng-content`に必要なテンプレートを投影する
- `TestBed.overrideComponent`でテンプレートを差し替えると特定ケースを検証しやすい

## 注意点
- `changes` Observableをテストする場合は`fakeAsync`や`tick()`を使って非同期を制御する
- ViewChildが非同期で設定される場合は`fixture.whenStable()`を利用する
- テンプレート参照変数が存在しないケースもテストし、例外が発生しないか確認する

## 関連技術
- Angular Testing Library
- `fakeAsync`, `tick`, `flush`
- HarnessベースのAngular Materialコンポーネントテスト
