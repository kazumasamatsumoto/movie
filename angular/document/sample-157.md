# #157 「QueryList の変更検知」

## 概要
`QueryList`の`changes` Observableを活用し、要素の追加・削除に反応してロジックを実行する方法を整理します。

## 学習目標
- QueryListの変更を検知する仕組みを理解する
- `changes`を購読して処理を自動化するパターンを習得する
- 購読解除やパフォーマンスに配慮した実装を学ぶ

## 技術ポイント
- **changes Observable**: 投影・ビューの更新で発火
- **購読解除**: `takeUntilDestroyed`または`DestroyRef`で安全に管理
- **初期処理**: `ngAfterViewInit`で初回処理を忘れず実行

## 📺 画面表示用コード（動画用）

```typescript
this.items.changes.subscribe(() => this.sync());
```

```typescript
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
```

```typescript
this.sync(); // ngAfterViewInitで初回処理
```

## 💻 詳細実装例（学習用）
```typescript
// marker-list.component.ts
import { AfterViewInit, Component, ElementRef, QueryList, ViewChildren } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-marker-list',
  standalone: true,
  templateUrl: './marker-list.component.html',
})
export class MarkerListComponent implements AfterViewInit {
  @ViewChildren('marker')
  markers!: QueryList<ElementRef<HTMLDivElement>>;

  items = ['A', 'B'];

  ngAfterViewInit(): void {
    this.applyMarkers();
    this.markers.changes
      .pipe(takeUntilDestroyed())
      .subscribe(() => this.applyMarkers());
  }

  add(): void {
    this.items = [...this.items, `Item ${Date.now()}`];
  }

  private applyMarkers(): void {
    this.markers.forEach((marker, index) => {
      marker.nativeElement.setAttribute('data-index', `${index}`);
    });
  }
}
```

```html
<!-- marker-list.component.html -->
<button type="button" (click)="add()">追加</button>
<div #marker *ngFor="let item of items">
  {{ item }}
</div>
```

## ベストプラクティス
- 変更検知のたびに重い処理が走らないよう軽量な更新ロジックを心がける
- `changes`購読は`takeUntilDestroyed`などを使って確実に解除する
- DOM操作や状態更新をまとめて行い、再描画回数を最小限にする

## 注意点
- `changes`は初期状態では発火しないので`ngAfterViewInit`などで最初に処理を実行する
- *ngIfや*ngForの更新頻度が高い場合、`changes`も頻繁に発火するためパフォーマンスへ注意
- QueryListを配列に変換したスナップショットは変更を追跡しないので、必要時に再取得する

## 関連技術
- `@ViewChildren` / `@ContentChildren`
- `DestroyRef` と `takeUntilDestroyed`
- Angular DevToolsでの描画確認
