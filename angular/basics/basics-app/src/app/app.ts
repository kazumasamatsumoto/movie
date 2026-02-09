import { Component, signal } from '@angular/core';
import { HeroList } from './hero-list/hero-list';
import { HeroListBad } from './hero-list-bad/hero-list-bad';

@Component({
  selector: 'app-root',
  imports: [HeroList, HeroListBad],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('basics-app');
  showBadExample = signal(false);
}
