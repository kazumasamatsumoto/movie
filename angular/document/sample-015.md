# #015 「imports 配列 - 依存関係の宣言」台本

四国めたん「imports 配列 - 依存関係の宣言について学びましょう！」
ずんだもん「imports配列って何？」
四国めたん「Standalone Componentで必要な依存関係を宣言する配列です」
ずんだもん「どんなものをインポートするの？」
四国めたん「CommonModule、FormsModule、RouterModuleなどのAngularモジュールや他のComponentです」
ずんだもん「順番は関係あるの？」
四国めたん「順番は関係ありませんが、読みやすさのために整理することが推奨されています」

---

## 📺 画面表示用コード

// 基本的なimports配列
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-basic-imports',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h1>{{title}}</h1>
      <p *ngIf="isVisible">表示中</p>
    </div>
  `
})
export class BasicImportsComponent {
  title = '基本的なインポート';
  isVisible = true;
}
```

// 複数のAngularモジュールをインポート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-multiple-imports',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ],
  template: `
    <div>
      <h2>複数インポート</h2>
      <form>
        <input [(ngModel)]="name" placeholder="名前">
        <button type="submit">送信</button>
      </form>
      <a routerLink="/home">ホーム</a>
    </div>
  `
})
export class MultipleImportsComponent {
  name = '';
}
```

// 他のComponentをインポート
```typescript
import { Component } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { SidebarComponent } from './sidebar/sidebar.component';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [
    HeaderComponent,
    FooterComponent,
    SidebarComponent
  ],
  template: `
    <div class="layout">
      <app-header></app-header>
      <div class="content">
        <app-sidebar></app-sidebar>
        <main>メインコンテンツ</main>
      </div>
      <app-footer></app-footer>
    </div>
  `
})
export class LayoutComponent {
  // 他のComponentを組み合わせて使用
}
```

// ディレクティブをインポート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgIf, NgFor } from '@angular/common';

@Component({
  selector: 'app-directives',
  standalone: true,
  imports: [NgIf, NgFor],
  template: `
    <div>
      <h2>ディレクティブ</h2>
      <p *ngIf="showMessage">メッセージを表示</p>
      <ul>
        <li *ngFor="let item of items">{{item}}</li>
      </ul>
    </div>
  `
})
export class DirectivesComponent {
  showMessage = true;
  items = ['項目1', '項目2', '項目3'];
}
```

// パイプをインポート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DatePipe, CurrencyPipe } from '@angular/common';

@Component({
  selector: 'app-pipes',
  standalone: true,
  imports: [CommonModule, DatePipe, CurrencyPipe],
  template: `
    <div>
      <h2>パイプ</h2>
      <p>日付: {{currentDate | date:'yyyy/MM/dd'}}</p>
      <p>価格: {{price | currency:'JPY'}}</p>
    </div>
  `
})
export class PipesComponent {
  currentDate = new Date();
  price = 1000;
}
```

// インポートの整理例
```typescript
import { Component } from '@angular/core';

// Angular標準モジュール
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

// カスタムComponent
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

// カスタムディレクティブ
import { HighlightDirective } from './directives/highlight.directive';

// カスタムパイプ
import { CustomPipe } from './pipes/custom.pipe';

@Component({
  selector: 'app-organized-imports',
  standalone: true,
  imports: [
    // Angular標準モジュール
    CommonModule,
    FormsModule,
    RouterModule,
    
    // カスタムComponent
    HeaderComponent,
    FooterComponent,
    
    // カスタムディレクティブ
    HighlightDirective,
    
    // カスタムパイプ
    CustomPipe
  ],
  template: `
    <div>
      <app-header></app-header>
      <main>
        <h1>整理されたインポート</h1>
        <p appHighlight>ハイライト</p>
        <p>{{text | custom}}</p>
      </main>
      <app-footer></app-footer>
    </div>
  `
})
export class OrganizedImportsComponent {
  text = 'カスタムパイプの例';
}
```

// 条件付きインポート
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-conditional-imports',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h2>条件付きインポート</h2>
      <p>必要な依存関係のみをインポート</p>
    </div>
  `
})
export class ConditionalImportsComponent {
  // 使用する機能に応じてインポートを選択
}
```

// インポートのベストプラクティス
```typescript
@Component({
  selector: 'app-best-practices',
  standalone: true,
  imports: [
    // 1. Angular標準モジュールを最初に
    CommonModule,
    FormsModule,
    
    // 2. カスタムComponentを次に
    HeaderComponent,
    FooterComponent,
    
    // 3. ディレクティブとパイプを最後に
    HighlightDirective,
    CustomPipe
  ],
  template: `
    <div>
      <h2>ベストプラクティス</h2>
      <ul>
        <li>Angular標準モジュールを最初に</li>
        <li>カスタムComponentを次に</li>
        <li>ディレクティブとパイプを最後に</li>
        <li>コメントでグループ化</li>
        <li>アルファベット順に整理</li>
      </ul>
    </div>
  `
})
export class BestPracticesComponent {
  // 読みやすく整理されたインポート
}
```

// インポートエラーの例
```typescript
// ❌ 間違ったインポート
@Component({
  selector: 'app-wrong-imports',
  standalone: true,
  imports: [
    // CommonModule,  // 必要なモジュールがインポートされていない
  ],
  template: `
    <div>
      <p *ngIf="true">エラーが発生</p>  <!-- *ngIfが使用できない -->
    </div>
  `
})
export class WrongImportsComponent {
  // エラー: *ngIfディレクティブが使用できない
}

// ✅ 正しいインポート
@Component({
  selector: 'app-correct-imports',
  standalone: true,
  imports: [CommonModule],  // CommonModuleをインポート
  template: `
    <div>
      <p *ngIf="true">正常に動作</p>  <!-- *ngIfが使用できる -->
    </div>
  `
})
export class CorrectImportsComponent {
  // 正常に動作
}
```
