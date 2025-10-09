# #089 「Lifecycle のベストプラクティス」

## 概要
Lifecycle Hooksを運用する際のベストプラクティスを体系的に整理し、保守しやすくパフォーマンスの高いコンポーネントを構築します。

## 学習目標
- フックの責務分離とコード整理のポイントを理解する
- 副作用とクリーンアップを対で設計する
- チームで共通ルールを制定する際の観点を学ぶ

## 技術ポイント
- **責務分離**: 初期化・監視・終了の3レイヤーで考える
- **副作用管理**: Signalsやサービスへ委譲してフック内を薄く保つ
- **クリーンアップ**: 取得したリソースは`ngOnDestroy`または`DestroyRef`で確実に解放


```typescript
ngOnInit() { this.initialize(); }
```

```typescript
ngOnDestroy() { this.dispose(); }
```

```typescript
effect(() => this.sync(), { scope: destroyRef });
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, DestroyRef, OnDestroy, OnInit, effect, inject, signal } from '@angular/core';

@Component({
  selector: 'app-lifecycle-best-practice',
  standalone: true,
  templateUrl: './lifecycle-best-practice.component.html',
})
export class LifecycleBestPracticeComponent implements OnInit, OnDestroy {
  private readonly destroyRef = inject(DestroyRef);
  readonly state = signal({ loading: false, data: [] as string[] });

  ngOnInit(): void {
    this.initialize();
    effect(
      () => {
        if (this.state().loading) {
          console.log('loading...');
        }
      },
      { scope: this.destroyRef },
    );
  }

  ngOnDestroy(): void {
    this.dispose();
  }

  private initialize(): void {
    this.state.set({ loading: true, data: [] });
    setTimeout(() => {
      this.state.set({ loading: false, data: ['A', 'B', 'C'] });
    }, 300);
  }

  private dispose(): void {
    console.log('クリーンアップ処理');
  }
}
```

```html
<p *ngIf="state().loading">読み込み中...</p>
<ul>
  <li @for (item of state().data; track item)>{{ item }}</li>
</ul>
```

## ベストプラクティス
- フックに直接ロジックを書かず、`initialize`, `dispose`などのメソッドを呼ぶだけにする
- クリーンアップは`ngOnDestroy`だけでなく`DestroyRef`による自動解放も併用する
- コメントやドキュメントで各フックの目的を明示し、チームメイトが理解しやすいようにする

## 注意点
- ミドルウェアやディレクティブなど複数箇所でLifecycleが絡む場合は責務が重複しやすい
- フックを過剰に追加すると可読性が落ちるため、必要なものだけ実装する
- `setTimeout`や外部APIを利用する際はエラーハンドリングもセットで設計する

## 関連技術
- Angular Style Guide
- Signalsと`DestroyRef`
- NxやSchematicsでのテンプレート化
