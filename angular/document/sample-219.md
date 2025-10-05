# #219 「コンテンツ投影の制約事項」

## 概要
Angular v20のコンテンツ投影における制約事項と制限について学習します。

## 学習目標
- コンテンツ投影の制約事項を理解する
- 制限を回避する方法を習得する
- 適切なアーキテクチャ設計を実現できるようになる

## 技術ポイント
- 制約事項
- 制限回避
- アーキテクチャ設計

## 📺 画面表示用コード

```html
<!-- 制約のある例 -->
<app-constrained-component>
  <!-- 投影後は親のデータバインディングが無効 -->
  <div>{{parentData}}</div> <!-- ❌ 動作しない -->
  <div [class]="parentClass"></div> <!-- ❌ 動作しない -->
  
  <!-- 投影コンポーネントのスコープで実行 -->
  <div>{{childData}}</div> <!-- ✅ 動作する -->
</app-constrained-component>
```

```html
<!-- 制約を回避する方法 -->
<app-workaround-component [parentData]="parentData" [parentClass]="parentClass">
  <div class="content">
    <!-- プロパティとしてデータを渡す -->
    <ng-template #contentTemplate let-data="parentData" let-className="parentClass">
      <div [class]="className">{{data}}</div>
    </ng-template>
  </div>
</app-workaround-component>
```

```typescript
// 制約を考慮したコンポーネント設計
@Component({
  selector: 'app-workaround-component',
  template: `
    <div class="container">
      <ng-content></ng-content>
      <!-- テンプレート参照を使用してデータを渡す -->
      <ng-container 
        [ngTemplateOutlet]="contentTemplate"
        [ngTemplateOutletContext]="{ 
          parentData: parentData, 
          parentClass: parentClass 
        }">
      </ng-container>
    </div>
  `
})
export class WorkaroundComponent {
  @Input() parentData: any;
  @Input() parentClass: string = '';
  
  @ContentChild('contentTemplate') contentTemplate!: TemplateRef<any>;
}
```

## 実践的な活用例

```html
<!-- イベントバインディングの制約 -->
<app-event-constrained>
  <!-- 親のイベントハンドラーは投影後は無効 -->
  <button (click)="parentClickHandler()">クリック</button> <!-- ❌ -->
  
  <!-- 子コンポーネントでイベントを処理 -->
  <button (click)="childClickHandler()">クリック</button> <!-- ✅ -->
</app-event-constrained>
```

## ベストプラクティス
- データフローを明確に設計する
- 適切なコンポーネント境界を設定する
- 制約を理解した上でアーキテクチャを設計する

## 注意点
- 投影後のデータバインディング制限
- イベントハンドラーのスコープ制限
- 依存性注入の制限

## 関連技術
- Component Architecture
- Data Flow Design
- Dependency Injection
