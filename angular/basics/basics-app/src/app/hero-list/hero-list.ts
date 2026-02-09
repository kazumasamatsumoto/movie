import { Component, OnInit, inject, signal, DestroyRef } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { HeroService, Hero } from '../hero.service';

@Component({
  selector: 'app-hero-list',
  imports: [],
  templateUrl: './hero-list.html',
  styleUrl: './hero-list.scss',
})
export class HeroList implements OnInit {
  private readonly heroService = inject(HeroService);
  private readonly destroyRef = inject(DestroyRef);

  heroes = signal<Hero[]>([]);
  loading = signal(false);

  ngOnInit(): void {
    this.loading.set(true);
    this.heroService.getHeroes()
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: (data) => {
          this.heroes.set(data);
          this.loading.set(false);
        },
        error: () => {
          this.loading.set(false);
        }
      });
  }
}
