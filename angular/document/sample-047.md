# #047 「(mouseenter) マウスイベント」台本

四国めたん「(mouseenter) マウスイベントについて学びましょう！」
ずんだもん「マウスの動きに反応するの？」
四国めたん「はい！マウスが要素に入ったり出たりした時に処理を実行できます」
ずんだもん「どんなイベントがあるの？」
四国めたん「mouseenter、mouseleave、mousemove、mouseoverなどがあります」
ずんだもん「ホバー効果に使える？」
四国めたん「はい！ツールチップ表示やスタイル変更などに活用できます」

---

## 📺 画面表示用コード

// 基本的なマウスイベント
```typescript
@Component({
  selector: 'app-mouse-basic',
  standalone: true,
  template: `
    <div class="mouse-demo">
      <h2>基本的なマウスイベント</h2>
      <div (mouseenter)="onMouseEnter()" 
           (mouseleave)="onMouseLeave()"
           [class.highlighted]="isHighlighted">
        マウスをホバーしてください
      </div>
      <p>状態: {{mouseStatus}}</p>
    </div>
  `,
  styles: [`
    .mouse-demo {
      padding: 20px;
    }
    div {
      padding: 20px;
      border: 2px solid #ccc;
      margin: 10px 0;
      transition: all 0.3s;
    }
    .highlighted {
      background-color: #ffffcc;
      border-color: #ffc107;
    }
  `]
})
export class MouseBasicComponent {
  isHighlighted = false;
  mouseStatus = 'マウスが外側';
  
  onMouseEnter() {
    this.isHighlighted = true;
    this.mouseStatus = 'マウスが要素内';
  }
  
  onMouseLeave() {
    this.isHighlighted = false;
    this.mouseStatus = 'マウスが外側';
  }
}
```

// ツールチップ表示
```typescript
@Component({
  selector: 'app-tooltip-demo',
  standalone: true,
  template: `
    <div class="tooltip-demo">
      <h2>ツールチップ表示</h2>
      <button (mouseenter)="showTooltip()" 
              (mouseleave)="hideTooltip()">
        ホバーしてツールチップを表示
      </button>
      <div *ngIf="showTooltipFlag" 
           class="tooltip">
        これはツールチップです
      </div>
    </div>
  `,
  styles: [`
    .tooltip-demo {
      padding: 20px;
      position: relative;
    }
    button {
      padding: 10px 20px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
    }
    .tooltip {
      position: absolute;
      top: 60px;
      left: 0;
      background-color: #333;
      color: white;
      padding: 8px 12px;
      border-radius: 4px;
      font-size: 14px;
    }
  `]
})
export class TooltipDemoComponent {
  showTooltipFlag = false;
  
  showTooltip() {
    this.showTooltipFlag = true;
  }
  
  hideTooltip() {
    this.showTooltipFlag = false;
  }
}
```

// マウス座標の取得
```typescript
@Component({
  selector: 'app-mouse-coordinates',
  standalone: true,
  template: `
    <div class="coordinates-demo">
      <h2>マウス座標の取得</h2>
      <div (mousemove)="onMouseMove($event)"
           (mouseenter)="onMouseEnter()"
           (mouseleave)="onMouseLeave()"
           class="tracking-area">
        マウスを動かしてください
      </div>
      <p *ngIf="isTracking">座標: X={{mouseX}}, Y={{mouseY}}</p>
    </div>
  `,
  styles: [`
    .coordinates-demo {
      padding: 20px;
    }
    .tracking-area {
      width: 300px;
      height: 200px;
      border: 2px solid #ccc;
      background-color: #f8f9fa;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 10px 0;
    }
  `]
})
export class MouseCoordinatesComponent {
  mouseX = 0;
  mouseY = 0;
  isTracking = false;
  
  onMouseMove(event: MouseEvent) {
    this.mouseX = event.clientX;
    this.mouseY = event.clientY;
  }
  
  onMouseEnter() {
    this.isTracking = true;
  }
  
  onMouseLeave() {
    this.isTracking = false;
  }
}
```
